"""
OpenAI API wrapper for Kids Video Agent.
Centralizes all OpenAI interactions with error handling and caching.
"""

import json
import os
from pathlib import Path
from typing import Any, Optional

from openai import OpenAI, APIError, APIConnectionError, RateLimitError


class OpenAIAPI:
    """Centralized OpenAI API client for the Kids Video Agent."""
    
    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-4o"):
        """
        Initialize OpenAI API client.
        
        Args:
            api_key: OpenAI API key (defaults to OPENAI_API_KEY env var)
            model: Default model to use (default: gpt-4o)
        """
        self.api_key = api_key or os.environ.get("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        
        self.client = OpenAI(api_key=self.api_key)
        self.model = model
    
    def generate_story(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.7,
        json_mode: bool = True,
    ) -> dict[str, Any]:
        """
        Generate a story using OpenAI with JSON response format.
        
        Args:
            system_prompt: System instruction for the model
            user_prompt: User's prompt/request
            temperature: Creativity level (0-1, default 0.7)
            json_mode: Whether to enforce JSON output format
        
        Returns:
            Parsed JSON response from the model
        
        Raises:
            ValueError: If response cannot be parsed as JSON
            APIError: If OpenAI API call fails
        """
        try:
            response_format = {"type": "json_object"} if json_mode else None
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                response_format=response_format,
                temperature=temperature,
            )
            
            content = response.choices[0].message.content
            return json.loads(content) if json_mode else {"content": content}
        
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse OpenAI response as JSON: {e}")
        except RateLimitError:
            raise APIError("Rate limit exceeded. Please retry after a delay.")
        except APIConnectionError as e:
            raise APIError(f"Connection error: {e}")
    
    def generate_text(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.7,
    ) -> str:
        """
        Generate plain text using OpenAI.
        
        Args:
            system_prompt: System instruction for the model
            user_prompt: User's prompt/request
            temperature: Creativity level (0-1, default 0.7)
        
        Returns:
            Plain text response from the model
        
        Raises:
            APIError: If OpenAI API call fails
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=temperature,
            )
            return response.choices[0].message.content
        except APIConnectionError as e:
            raise APIError(f"Connection error: {e}")
    
    def generate_with_retries(
        self,
        system_prompt: str,
        user_prompt: str,
        max_retries: int = 3,
        temperature: float = 0.7,
        json_mode: bool = True,
    ) -> dict[str, Any]:
        """
        Generate with automatic retry on failure.
        
        Args:
            system_prompt: System instruction for the model
            user_prompt: User's prompt/request
            max_retries: Maximum number of retries
            temperature: Creativity level
            json_mode: Whether to enforce JSON output format
        
        Returns:
            Parsed JSON response from the model
        
        Raises:
            APIError: If all retries fail
        """
        last_error = None
        for attempt in range(max_retries):
            try:
                return self.generate_story(system_prompt, user_prompt, temperature, json_mode)
            except APIError as e:
                last_error = e
                print(f"Attempt {attempt + 1} failed: {e}. Retrying...")
                if attempt < max_retries - 1:
                    import time
                    time.sleep(2 ** attempt)  # Exponential backoff
        
        raise last_error or APIError("Failed after max retries")
    
    def save_response(self, data: dict, output_path: Path) -> None:
        """
        Save API response to a JSON file.
        
        Args:
            data: Data to save
            output_path: Path to save the JSON file
        """
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )


# Singleton instance
_api_instance: Optional[OpenAIAPI] = None


def get_openai_api(model: str = "gpt-4o") -> OpenAIAPI:
    """Get or create a singleton OpenAI API instance."""
    global _api_instance
    if _api_instance is None:
        _api_instance = OpenAIAPI(model=model)
    return _api_instance
