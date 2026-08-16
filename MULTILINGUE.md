# Support multilingue – Anglais, Espagnol, Arabe, Wolof

## 1. Adapter le prompt principal

### Fichier `screenwriter.py`

Modifie la section `SYSTEM` pour changer de langue :

**Franç·±ais (par défaut) :**
```python
SYSTEM = """You write safe, cheerful French stories for children aged 1-7.
Return only valid JSON. Use cute animals, simple toys, bright colours and a happy ending.
No violence, fear, sadness, brands, copyrighted characters, personal data, calls to buy, or scary themes.
Voiceover phrases must be short and simple French."""
```

**Anglais :**
```python
SYSTEM = """You write safe, cheerful English stories for children aged 1-7.
Return only valid JSON. Use cute animals, simple toys, bright colors and a happy ending.
No violence, fear, sadness, brands, copyrighted characters, personal data, calls to buy, or scary themes.
Voiceover phrases must be short and simple English."""
```

**Espagnol :**
```python
SYSTEM = """Escribes historias seguras y alegres en españ⸱ol para niñ·±·os de 1-7 añ⸱os.
Return only valid JSON. Use cute animals, simple toys, bright colors and a happy ending.
No violence, fear, sadness, brands, copyrighted characters, personal data, calls to buy, or scary themes.
Voiceover phrases must be short and simple Spanish."""
```

**Arabe :**
```python
SYSTEM = """You write safe, cheerful Arabic stories for children aged 1-7.
Return only valid JSON. Use cute animals, simple toys, bright colors and a happy ending.
No violence, fear, sadness, brands, copyrighted characters, personal data, calls to buy, or scary themes.
Voiceover phrases must be short and simple Arabic."""
```

**Wolof :**
```python
SYSTEM = """You write safe, cheerful Wolof stories for children aged 1-7.
Return only valid JSON. Use cute animals, simple toys, bright colors and a happy ending.
No violence, fear, sadness, brands, copyrighted characters, personal data, calls to buy, or scary themes.
Voiceover phrases must be short and simple Wolof."""
```

---

## 2. Adapter la voix ElevenLabs

### Voix recommand ées par langue

| Langue | Voix ElevenLabs | ID |
|--------|----------------|-----|
| Français | Rachel | `Rachel` |
| Anglais | Rachel / Adam | `Rachel`, `Adam` |
| Espagnol | Ana | `Ana` |
| Arabe | Matthew (arabe) | `Matthew` |
| Wolof | Utiliser une voix anglaise douce | `Domi` |

### Modifier `voiceover.py`

```python
VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID", "Rachel")  # Change selon la langue
```

Ou dans `agent_config.yaml` :
```yaml
voice:
  voice_id: Ana  # Pour l'espagnol
  model: eleven_multilingual_v2
```

---

## 3. Exemples de titres et descriptions

### Anglais

**YouTube :**
- Titre : `Lulu's Red Ball | Story for Kids 1–7 Years`
- Description :
```
A colorful and cheerful story for children aged 1 to 7.
Lulu the rabbit discovers a red ball in a magical garden.

Created by Kids Video Agent (AI).

Subscribe for more stories!
```
- Tags : `kids story, children video, cartoon, bedtime stories, english stories`

**TikTok :**
- Légende : `Lulu's Red Ball 🎈 #kids #story #english #cartoon #children`

---

### Espagnol

**YouTube :**
- Titre : `La Pelota Roja de Lulu | Cuento para niñ·±·os 1–7 añ⸱os`
- Description :
```
Una historia colorida y alegre para niñ·±·os de 1 a 7 añ⸱os.
Lulu el conejo descubre una pelota roja en un jardí·±n m á gico.

Creado por Kids Video Agent (IA).

Suscrí·±bete para m á s cuentos!
```
- Tags : `cuento infantil, video niñ·±·os, dibujos animados, historias en españ⸱ol`

**TikTok :**
- Légende : `La Pelota Roja de Lulu 🎈 #niñ·±·os #cuento #españ·±·ol #dibujos`

---

### Arabe

**YouTube :**
- Titre : `كرة لولو الحمراء | قصة للأطفال 1–7 سنوات`
- Description :
```
قصة ملونة ومبهجة للأطفال من 1 إلى 7 سنوات.
لولو الأرنب تكتشف كرة حمراء في حديقة سحرية.

تم الإنشاء بواسطة Kids Video Agent (AI).

اشترك للمزيد من القصص!
```
- Tags : `قصة أطفال, فيديو للأطفال, كرتون, قصص عربية`

**TikTok :**
- Légende : `كرة لولو الحمراء 🎈 #أطفال #قصة #عربي #كرتون`

---

### Wolof

**YouTube :**
- Titre : `Balle bu Lulu | Xaajal bu ndaw 1–7 at`
- Description :
```
Xaajal bu melax te yaatu ngir ndaw yi 1 ba 7 at.
Lulu laqu dafa fekk balle bu xonk ci jardin bu mag.

Sosu ko Kids Video Agent (AI).

Nanga subscribe ngir yeneen xaajal!
```
- Tags : `xaajal, ndaw, wolof, senegal`

**TikTok :**
- Légende : `Balle bu Lulu 🎈 #wolof #senegal #xaajal #ndaw`

---

## 4. Straté·±gie de publication par langue

### Anglais (marché·± global)

- **YouTube** : 3–5 vidé ·os/semaine
- **TikTok** : 1–2/jour
- **Concurrence** : é ·levé·±e, mais audience trè·±s large
- **Moné·±tisation** : CPM plus é ·levé·± (2–5 € pour 1000 vues)

### Espagnol (marché·± hispanophone)

- **YouTube** : 3–5 vidé ·os/semaine
- **TikTok** : 1/jour
- **Pays cibles** : Espagne, Mexique, Argentine, Colombie
- **Moné·±tisation** : CPM moyen (1–3 € pour 1000 vues)

### Arabe (marché·± MENA)

- **YouTube** : 2–4 vidé ·os/semaine
- **TikTok** : 1/jour
- **Pays cibles** : Arabie Saoudite, Égypte, Maroc, Algé·±rie
- **Moné·±tisation** : CPM variable (0,5–2 € pour 1000 vues)

### Wolof (marché·± s éné·±galais/africain)

- **YouTube** : 2–3 vidé ·os/semaine
- **TikTok** : 1/jour
- **Pays cibles** : Sé ·né·±gal, Gambie, Mauritanie
- **Moné·±tisation** : CPM plus bas, mais niche peu concurrentielle
- **Opportunit é s** : Partenariats locaux, marques africaines

---

## 5. Créer plusieurs dépô·±·ts par langue

Pour une meilleure organisation :

- `kids-video-agent-fr` (franç·±ais)
- `kids-video-agent-en` (anglais)
- `kids-video-agent-es` (espagnol)
- `kids-video-agent-ar` (arabe)
- `kids-video-agent-wo` (wolof)

Chaque dé ·pô·±·t a son propre `agent_config.yaml` avec les thè·±mes adapt é s à la culture locale.

---

## 6. Exemple de configuration par langue

### `agent_config.yaml` – Anglais

```yaml
themes:
  - magical garden
  - colorful bedroom
  - enchanted park
  - happy beach
  - toy forest

animals:
  - rabbit
  - cat
  - dog
  - bird
  - elephant
  - lion cub
  - giraffe

toys:
  - red ball
  - yellow cube
  - green car
  - pink teddy
  - colorful puzzle

colors:
  - red, yellow, blue
  - green, orange, pink
  - blue, purple, yellow
```

### `agent_config.yaml` – Espagnol

```yaml
themes:
  - jardí·±n m á gico
  - habitaci ó n colorida
  - parque encantado
  - playa alegre
  - bosque de juguetes

animals:
  - conejo
  - gato
  - perro
  - p á jaro
  - elefante
  - le ó n
  - jirafa
```

---

## 7. Traduction automatique (optionnel)

Tu peux utiliser un LLM pour traduire automatiquement :

```python
# Ajouter dans screenwriter.py
TRANSLATE_PROMPT = """Translate this story to {language}:
{story_json}

Keep the same structure, just translate the text.
Return only valid JSON."""
```

---

## 8. Ressources utiles

- **ElevenLabs Voices** : https://elevenlabs.io/voice-library
- **YouTube Multi-language** : https://support.google.com/youtube/answer/6279017
- **TikTok Global** : https://www.tiktok.com/business/en/inspiration

---

## 9. Checklist multilingue

- [ ] Choisir la langue cible
- [ ] Adapter le prompt `SYSTEM` dans `screenwriter.py`
- [ ] Changer la voix ElevenLabs
- [ ] Traduire les titres et descriptions
- [ ] Adapter les hashtags TikTok
- [ ] Publier sur YouTube/TikTok dans la bonne langue
- [ ] Analyser les performances et ajuster

---

Bon courage pour tes vidé ·os multilingues ! 🌍🎈🧸
