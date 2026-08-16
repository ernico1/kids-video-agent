import json
import os
from pathlib import Path

from elevenlabs import ElevenLabs

ROOT = Path(__file__).parent
client = ElevenLabs(api_key=os.environ["ELEVENLABS_API_KEY"])
VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID", "Rachel")


def main():
    story = json.loads((ROOT / "output" / "story.json").read_text(encoding="utf-8"))
    audio_dir = ROOT / "output" / "audio"
    audio_dir.mkdir(parents=True, exist_ok=True)
    for scene in story["scenes"]:
        audio = client.text_to_speech.convert(
            voice_id=VOICE_ID,
            model_id="eleven_multilingual_v2",
            text=scene["voiceover"],
        )
        path = audio_dir / f"scene_{scene['id']:02d}_voiceover.mp3"
        with path.open("wb") as handle:
            for chunk in audio:
                handle.write(chunk)


if __name__ == "__main__":
    main()