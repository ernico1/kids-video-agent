#!/usr/bin/env python3
"""
run_all.py
Lance le pipeline complet : histoire → images → voix → montage.
Usage :
  python run_all.py
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent

# Import the centralized API modules
from openai_api import get_openai_api
from elevenlabs_api import get_elevenlabs_api

# Import moviepy for video editing
from moviepy.editor import AudioFileClip, ImageClip, concatenate_videoclips
import requests
import yaml


def load_config():
    """Load configuration from agent_config.yaml"""
    config_path = ROOT / "agent_config.yaml"
    return yaml.safe_load(config_path.read_text(encoding="utf-8"))


def generate_story(config):
    """Step 1: Generate story using OpenAI API"""
    print("=== Step 1: Generating story ===")
    
    openai_api = get_openai_api()
    
    system_prompt = """You write safe, cheerful French stories for children aged 1-7.
Return only valid JSON. Use cute animals, simple toys, bright colours and a happy ending.
No violence, fear, sadness, brands, copyrighted characters, personal data, calls to buy, or scary themes.
Voiceover phrases must be short and simple French."""
    
    user_prompt = f"""Create a French children's video story as JSON.
Use 3 to 6 scenes, total 30 to 90 seconds.
Themes: {config['themes']}
Animals: {config['animals']}
Toys: {config['toys']}
Colours: {config['colors']}
Return this exact schema:
{{
  "title": "...",
  "scenes": [
    {{"id": 1, "duration_seconds": 6, "visual": "...", "voiceover": "..."}}
  ],
  "total_duration_seconds": 30
}}"""
    
    story = openai_api.generate_story(
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        temperature=0.7,
        json_mode=True
    )
    
    output_dir = ROOT / "output"
    output_dir.mkdir(exist_ok=True)
    openai_api.save_response(story, output_dir / "story.json")
    
    print(f"✓ Story generated: {story['title']}")
    print(f"  Scenes: {len(story['scenes'])}, Duration: {story['total_duration_seconds']}s")
    return story


def generate_images(story, config):
    """Step 2: Generate scene images using DALL-E 3"""
    print("\n=== Step 2: Generating scene images ===")
    
    openai_api = get_openai_api(model="gpt-4o")
    scenes_dir = ROOT / "output" / "scenes"
    scenes_dir.mkdir(parents=True, exist_ok=True)
    
    for scene in story["scenes"]:
        prompt = (
            f"{scene['visual']}. Cute original cartoon for children aged 1-7, "
            "bright happy colors, soft rounded shapes, friendly animals and toys, "
            "safe cheerful mood, no text, no logos, no copyrighted characters."
        )
        
        # Use OpenAI client directly for DALL-E (not in our wrapper yet)
        from openai import OpenAI
        import os
        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        
        result = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1
        )
        
        image = requests.get(result.data[0].url, timeout=60)
        image.raise_for_status()
        
        image_path = scenes_dir / f"scene_{scene['id']:02d}.png"
        image_path.write_bytes(image.content)
        print(f"✓ Generated scene {scene['id']}: {image_path.name}")


def generate_voiceovers(story, config):
    """Step 3: Generate voiceovers using ElevenLabs API"""
    print("\n=== Step 3: Generating voiceovers ===")
    
    elevenlabs_api = get_elevenlabs_api(
        voice_id=config['voice'].get('voice_id', 'Rachel')
    )
    
    audio_dir = ROOT / "output" / "audio"
    audio_dir.mkdir(parents=True, exist_ok=True)
    
    texts = [scene["voiceover"] for scene in story["scenes"]]
    
    audio_paths = elevenlabs_api.generate_batch(
        texts=texts,
        output_dir=audio_dir,
        model=config['voice'].get('model', 'eleven_multilingual_v2'),
        stability=0.5,
        similarity_boost=0.75
    )
    
    print(f"✓ Generated {len(audio_paths)} voiceovers")


def create_video(story, config):
    """Step 4: Assemble video from images and audio"""
    print("\n=== Step 4: Creating final video ===")
    
    clips = []
    for scene in story["scenes"]:
        image_path = ROOT / "output" / "scenes" / f"scene_{scene['id']:02d}.png"
        audio_path = ROOT / "output" / "audio" / f"voiceover_{scene['id']-1:02d}.mp3"
        
        audio = AudioFileClip(str(audio_path))
        duration = max(float(scene["duration_seconds"]), audio.duration)
        clip = ImageClip(str(image_path)).set_duration(duration).set_audio(audio)
        clips.append(clip)
    
    final = concatenate_videoclips(clips, method="compose")
    output_path = ROOT / "output" / "kids_video.mp4"
    
    print(f"Writing video to {output_path}...")
    final.write_videofile(
        str(output_path),
        fps=config['style'].get('fps', 24),
        codec="libx264",
        audio_codec="aac",
        logger=None,
        verbose=False
    )
    
    print(f"✓ Video created: {output_path}")
    return output_path


def main():
    try:
        print("=" * 60)
        print("Kids Video Agent - Complete Pipeline")
        print("=" * 60)
        
        # Load configuration
        config = load_config()
        
        # Run pipeline steps
        story = generate_story(config)
        generate_images(story, config)
        generate_voiceovers(story, config)
        video_path = create_video(story, config)
        
        print("\n" + "=" * 60)
        print("✓ Pipeline completed successfully!")
        print(f"Video saved to: {video_path}")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
