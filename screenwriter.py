import json
import os
from pathlib import Path

import yaml
from openai import OpenAI

ROOT = Path(__file__).parent
CONFIG = yaml.safe_load((ROOT / "agent_config.yaml").read_text(encoding="utf-8"))
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

SYSTEM = """You write safe, cheerful French stories for children aged 1-7.
Return only valid JSON. Use cute animals, simple toys, bright colours and a happy ending.
No violence, fear, sadness, brands, copyrighted characters, personal data, calls to buy, or scary themes.
Voiceover phrases must be short and simple French."""


def main():
    prompt = f"""Create a French children's video story as JSON.
Use 3 to 6 scenes, total 30 to 90 seconds.
Themes: {CONFIG['themes']}
Animals: {CONFIG['animals']}
Toys: {CONFIG['toys']}
Colours: {CONFIG['colors']}
Return this exact schema:
{{
  \"title\": \"...\",
  \"scenes\": [
    {{\"id\": 1, \"duration_seconds\": 6, \"visual\": \"...\", \"voiceover\": \"...\"}}
  ],
  \"total_duration_seconds\": 30
}}"""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": SYSTEM}, {"role": "user", "content": prompt}],
        response_format={"type": "json_object"},
        temperature=0.7,
    )
    story = json.loads(response.choices[0].message.content)
    output = ROOT / "output"
    output.mkdir(exist_ok=True)
    (output / "story.json").write_text(json.dumps(story, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(story, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()