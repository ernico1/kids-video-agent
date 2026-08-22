"""
ElevenLabs API wrapper for Kids Video Agent.
Centralizes all text-to-speech interactions with error handling and caching.
"""

import os
from pathlib import Path
from typing import Optional

from elevenlabs import ElevenLabs, VoiceSettings
from elevenlabs.client import ElevenLabsClient


class ElevenLabsAPI:
    """Centralized ElevenLabs API client for the Kids Video Agent."""
    
    def __init__(self, api_key: Optional[str] = None, voice_id: str = "Rachel"):
        """
        Initialize ElevenLabs API client.
        
        Args:
            api_key: ElevenLabs API key (defaults to ELEVENLABS_API_KEY env var)
            voice_id: Default voice ID to use (default: Rachel)
        """
        self.api_key = api_key or os.environ.get("ELEVENLABS_API_KEY")
        if not self.api_key:
            raise ValueError("ELEVENLABS_API_KEY not found in environment variables")
        
        self.client = ElevenLabs(api_key=self.api_key)
        self.voice_id = voice_id
    
    def generate_speech(
        self,
        text: str,
        voice_id: Optional[str] = None,
        model: str = "eleven_multilingual_v2",
        stability: float = 0.5,
        similarity_boost: float = 0.75,
    ) -> bytes:
        """
        Generate speech audio from text.
        
        Args:
            text: Text to convert to speech
            voice_id: Voice ID to use (defaults to self.voice_id)
            model: Model to use (default: eleven_multilingual_v2)
            stability: Voice stability (0-1, default 0.5)
            similarity_boost: Voice similarity boost (0-1, default 0.75)
        
        Returns:
            Audio bytes in MP3 format
        
        Raises:
            ValueError: If text is empty
            Exception: If API call fails
        """
        if not text or not text.strip():
            raise ValueError("Text cannot be empty")
        
        voice_id = voice_id or self.voice_id
        
        try:
            audio = self.client.generate(
                text=text,
                voice=self.client.voices.get(voice_id),
                model=model,
                voice_settings=VoiceSettings(
                    stability=stability,
                    similarity_boost=similarity_boost,
                ),
            )
            return b"".join(audio)
        except Exception as e:
            raise Exception(f"Failed to generate speech: {e}")
    
    def generate_and_save(
        self,
        text: str,
        output_path: Path,
        voice_id: Optional[str] = None,
        model: str = "eleven_multilingual_v2",
        stability: float = 0.5,
        similarity_boost: float = 0.75,
    ) -> Path:
        """
        Generate speech and save to file.
        
        Args:
            text: Text to convert to speech
            output_path: Path to save the audio file
            voice_id: Voice ID to use (defaults to self.voice_id)
            model: Model to use (default: eleven_multilingual_v2)
            stability: Voice stability (0-1, default 0.5)
            similarity_boost: Voice similarity boost (0-1, default 0.75)
        
        Returns:
            Path to the saved audio file
        
        Raises:
            ValueError: If text is empty or path is invalid
            Exception: If API call or file write fails
        """
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        audio_bytes = self.generate_speech(
            text=text,
            voice_id=voice_id,
            model=model,
            stability=stability,
            similarity_boost=similarity_boost,
        )
        
        output_path.write_bytes(audio_bytes)
        return output_path
    
    def get_available_voices(self) -> dict:
        """
        Get list of available voices.
        
        Returns:
            Dictionary of voice IDs and their details
        """
        try:
            voices = self.client.voices.get_all()
            return {voice.voice_id: voice.name for voice in voices}
        except Exception as e:
            raise Exception(f"Failed to get available voices: {e}")
    
    def generate_batch(
        self,
        texts: list[str],
        output_dir: Path,
        voice_id: Optional[str] = None,
        model: str = "eleven_multilingual_v2",
        stability: float = 0.5,
        similarity_boost: float = 0.75,
    ) -> list[Path]:
        """
        Generate speech for multiple texts and save to files.
        
        Args:
            texts: List of texts to convert to speech
            output_dir: Directory to save audio files
            voice_id: Voice ID to use (defaults to self.voice_id)
            model: Model to use (default: eleven_multilingual_v2)
            stability: Voice stability (0-1, default 0.5)
            similarity_boost: Voice similarity boost (0-1, default 0.75)
        
        Returns:
            List of paths to saved audio files
        
        Raises:
            ValueError: If texts list is empty
            Exception: If API call or file write fails
        """
        if not texts:
            raise ValueError("Texts list cannot be empty")
        
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        output_paths = []
        for i, text in enumerate(texts):
            output_path = output_dir / f"voiceover_{i:02d}.mp3"
            path = self.generate_and_save(
                text=text,
                output_path=output_path,
                voice_id=voice_id,
                model=model,
                stability=stability,
                similarity_boost=similarity_boost,
            )
            output_paths.append(path)
            print(f"Generated audio {i + 1}/{len(texts)}: {path}")
        
        return output_paths


# Singleton instance
_api_instance: Optional[ElevenLabsAPI] = None


def get_elevenlabs_api(voice_id: str = "Rachel") -> ElevenLabsAPI:
    """Get or create a singleton ElevenLabs API instance."""
    global _api_instance
    if _api_instance is None:
        _api_instance = ElevenLabsAPI(voice_id=voice_id)
    return _api_instance
