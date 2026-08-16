import json
import os
from pathlib import Path

import requests
from openai import OpenAI

ROOT = Path(__file__).parent
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


def main():
    story = json.loads((ROOT / "output" / "story.json").read_text(encoding="utf-8"))
    scenes_dir = ROOT / "output" / "scenes"
    scenes_dir.mkdir(parents=True, exist_ok=True)
    for scene in story["scenes"]:
        prompt = (
            f"{scene['visual']}. Cute original cartoon for children aged 1-7, "
            "bright happy colors, soft rounded shapes, friendly animals and toys, "
            "safe cheerful mood, no text, no logos, no copyrighted characters."
        )
        result = client.images.generate(model="dall-e-3", prompt=prompt, size="1024x1024", quality="standard", n=1)
        image = requests.get(result.data[0].url, timeout=60)
        image.raise_for_status()
        (scenes_dir / f"scene_{scene['id']:02d}.png").write_bytes(image.content)


if __name__ == "__main__":
    main()