# Kids Video Agent

Agent Python qui fabrique une courte video originale et coloree pour enfants de 1 a 7 ans : histoire en francais, images cartoon, voix off et montage MP4.

## Pipeline

1. `screenwriter.py` cree une histoire JSON.
2. `art_director.py` cree une image originale par scene.
3. `voiceover.py` produit la voix off.
4. `editor.py` assemble les scenes en MP4.

## Installation locale

```bash
pip install -r requirements.txt
export OPENAI_API_KEY="..."
export ELEVENLABS_API_KEY="..."
python screenwriter.py
python art_director.py
python voiceover.py
python editor.py
```

La video finale est `output/kids_video.mp4`.

## GitHub Actions

Ajoute ces secrets dans `Settings > Secrets and variables > Actions` :

- `OPENAI_API_KEY`
- `ELEVENLABS_API_KEY`
- `ELEVENLABS_VOICE_ID` (optionnel)

Le workflow peut etre lance depuis l'onglet Actions et est aussi programme quotidiennement a 10:00 UTC.

## Securite contenu enfants

Le prompt impose des histoires originales, joyeuses, sans violence ni peur, sans personnages proteges, sans publicite ni collecte de donnees personnelles. Verifie chaque video avant publication et configure correctement l'audience "destinee aux enfants" sur YouTube.

## Attention aux couts

Les appels LLM, image et voix utilisent des API payantes selon ton fournisseur. GitHub Actions ne fournit pas les cles API : elles doivent etre ajoutees comme secrets.