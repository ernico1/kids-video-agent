#!/usr/bin/env python3
"""
Pipeline complet pour gén\u00e9rer une vid\u00e9o pour enfants
Ex\u00e9cute dans l'ordre: sc\u00e9nario \u2192 voix \u2192 images \u2192 montage
"""

import os
import sys
from datetime import datetime

def main():
    try:
        # Cr\u00e9ation du dossier de sortie
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)
        
        # R\u00e9cup\u00e9ration du topic depuis les arguments ou env
        topic = sys.argv[1] if len(sys.argv) > 1 else os.getenv('VIDEO_TOPIC', 'Jungle animals')
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        print(f"\ud83c\udfac G\u00e9n\u00e9ration vid\u00e9o: {topic}")
        print(f"\ud83d\udcc1 Dossier de sortie: {output_dir}/{timestamp}")
        
        # 1. Sc\u00e9nario
        print("\n\ud83d\udddd\ufe0f \u00c9tape 1: G\u00e9n\u00e9ration du sc\u00e9nario...")
        from screenwriter import generate_script
        script = generate_script(topic)
        
        # 2. Voix off
        print("\n\ud83c\udf99\ufe0f \u00c9tape 2: G\u00e9n\u00e9ration de la voix off...")
        from voiceover import generate_voiceover
        audio_path = generate_voiceover(script, f"{output_dir}/{timestamp}/voiceover.mp3")
        
        # 3. Images
        print("\n\ud83c\udfa8 \u00c9tape 3: G\u00e9n\u00e9ration des images...")
        from art_director import generate_images
        image_paths = generate_images(script, f"{output_dir}/{timestamp}/images")
        
        # 4. Montage
        print("\n\u2702\ufe0f \u00c9tape 4: Montage vid\u00e9o...")
        from editor import create_video
        video_path = create_video(image_paths, audio_path, f"{output_dir}/{timestamp}/final.mp4")
        
        print(f"\n\u2705 Vid\u00e9o g\u00e9n\u00e9r\u00e9e: {video_path}")
        
    except Exception as e:
        print(f"\n\u274c Erreur: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
