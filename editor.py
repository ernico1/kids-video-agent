import json
from pathlib import Path

from moviepy.editor import AudioFileClip, ImageClip, concatenate_videoclips

ROOT = Path(__file__).parent


def main():
    story = json.loads((ROOT / "output" / "story.json").read_text(encoding="utf-8"))
    clips = []
    for scene in story["scenes"]:
        image_path = ROOT / "output" / "scenes" / f"scene_{scene['id']:02d}.png"
        audio_path = ROOT / "output" / "audio" / f"scene_{scene['id']:02d}_voiceover.mp3"
        audio = AudioFileClip(str(audio_path))
        duration = max(float(scene["duration_seconds"]), audio.duration)
        clip = ImageClip(str(image_path)).set_duration(duration).set_audio(audio)
        clips.append(clip)
    final = concatenate_videoclips(clips, method="compose")
    output = ROOT / "output" / "kids_video.mp4"
    final.write_videofile(str(output), fps=24, codec="libx264", audio_codec="aac", logger=None)
    print(output)


if __name__ == "__main__":
    main()