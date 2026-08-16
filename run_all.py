#!/usr/bin/env python3
"""
run_all.py
Lance le pipeline complet : histoire → images → voix → montage.
Usage :
  python run_all.py
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent


def run_script(name: str):
    script = ROOT / name
    if not script.exists():
        print(f"Script introuvable : {script}")
        sys.exit(1)
    print(f"--- Lancement : {name} ---")
    result = subprocess.run([sys.executable, str(script)], cwd=ROOT)
    if result.returncode != 0:
        print(f"Erreur dans {name}")
        sys.exit(1)


def main():
    print("=== Kids Video Agent - Pipeline complet ===")
    run_script("screenwriter.py")
    run_script("art_director.py")
    run_script("voiceover.py")
    run_script("editor.py")
    print("=== Pipeline terminé ===")
    print("Vidео finale : output/kids_video.mp4")


if __name__ == "__main__":
    main()
