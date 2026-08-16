# Guide de configuration et publication

## 1. Configurer les secrets GitHub

### Étape 1 : Obtenir les clés API

**OpenAI :**
1. Va sur https://platform.openai.com/api-keys
2. Crè·±e une nouvelle clé API
3. Copie la clé (commence par `sk-...`)

**ElevenLabs :**
1. Va sur https://elevenlabs.io/docs
2. Connecte-toi ou crè·±e un compte
3. Trouve ta clé API dans les paramètres
4. Copie la clé

**Voice ID (optionnel) :**
- Dans ElevenLabs, choisis une voix (ex. "Rachel", "Domi", "Antoni")
- Copie l'ID de la voix (ex. `Rachel`)

### Étape 2 : Ajouter les secrets dans GitHub

1. Va sur https://github.com/ernico1/kids-video-agent
2. Clique sur **Settings** (en haut)
3. Dans le menu de gauche, clique sur **Secrets and variables** → **Actions**
4. Clique sur **New repository secret**
5. Ajoute les 3 secrets :

| Nom | Valeur |
|-----|--------|
| `OPENAI_API_KEY` | Ta clé OpenAI (`sk-...`) |
| `ELEVENLABS_API_KEY` | Ta clé ElevenLabs |
| `ELEVENLABS_VOICE_ID` | `Rachel` (ou autre voix) |

6. Clique sur **Add secret** pour chaque

### Étape 3 : Tester le workflow

1. Clique sur **Actions** (en haut)
2. Sélectionne **Generate Kids Video**
3. Clique sur **Run workflow** (bouton vert)
4. Attends 5–10 minutes
5. La vidéo sera dans **Artifacts** en bas de page

---

## 2. Personnaliser l'agent

### Modifier `agent_config.yaml`

Ouvre le fichier et change :

**Thè·±mes :**
```yaml
themes:
  - jardin magique
  - chambre coloree
  - parc enchante
  - plage joyeuse
  - foret des jouets
  # Ajoute tes propres thè·±mes
```

**Animaux :**
```yaml
animals:
  - lapin
  - chat
  - chien
  - oiseau
  - elephant
  # Ajoute tes animaux préfé·±ré·±s
```

**Jouets :**
```yaml
toys:
  - ballon rouge
  - cube jaune
  - voiture verte
  - peluche rose
  # Ajoute tes jouets
```

**Couleurs :**
```yaml
colors:
  - rouge, jaune, bleu
  - vert, orange, rose
  - bleu, violet, jaune
  # Tes palettes préfé·±ré·±es
```

**Duré·±e :**
```yaml
generation:
  target_duration_min: 30
  target_duration_max: 60  # 30–60 secondes
  scenes_min: 3
  scenes_max: 5
```

**Sé·±curité·± :**
```yaml
safety:
  no_violence: true
  no_fear: true
  always_happy_ending: true
  max_words_per_voiceover: 8  # phrases très courtes
```

---

## 3. Publier sur YouTube

### Étape 1 : Préparer la vidéo

1. Télécharge l'artefact depuis GitHub Actions
2. Vérifie la vidéo (qualité·±, audio, contenu)
3. Renomme-la si besoin (ex. `le_ballon_rouge_de_lulu.mp4`)

### Étape 2 : Créer une chaîne YouTube

1. Va sur https://youtube.com
2. Connecte-toi avec ton compte Google
3. Crè·±e une chaîne (ex. "Histoires Coloré·±es")
4. Ajoute un logo et une banniè·±re coloré·±s

### Étape 3 : Uploader la vidéo

1. Clique sur **Cré·±er** (camé·±ra +) → **Uploader une vidé ·o**
2. Sélectionne ton fichier MP4
3. Remplis les informations :

**Titre :**
```
Le Ballon Rouge de Lulu | Histoire pour enfants 1–7 ans
```

**Description :**
```
Une histoire coloré·±e et joyeuse pour les enfants de 1 à 7 ans.
Animaux mignons, jouets et couleurs vives !

Cré·±é·± par Kids Video Agent (IA).

Abonne-toi pour plus d'histoires !
```

**Miniature :**
- Utilise une image de la vidéo ou crè·±e une miniature coloré·±e avec Canva

**Audience :**
- **OUI, destiné aux enfants** (trè·±s important pour COPPA)

**Tags :**
```
histoire pour enfants, video enfant, dessin anime, conte, kids video, french stories
```

4. Clique sur **Suivant** → **Suivant** → **Publier**

### Étape 4 : Optimiser pour YouTube Kids

- Active **Made for Kids** dans YouTube Studio
- Désactive les commentaires (optionnel pour contenu enfants)
- Ajoute la vidé ·o à une playlist "Histoires pour enfants"

---

## 4. Publier sur TikTok

### Étape 1 : Adapter le format

Pour TikTok, privilé·±gie le format **9:16 (vertical)** :

1. Modifie `agent_config.yaml` :
```yaml
style:
  video_format: "9:16"  # au lieu de "16:9"
```

2. Ou recadre la vidé ·o avec un outil comme CapCut

### Étape 2 : Créer un compte TikTok

1. Télécharge l'app TikTok ou va sur https://tiktok.com
2. Crè·±e un compte (ex. "@histoires_colorees")
3. Ajoute une photo de profil coloré·±e

### Étape 3 : Publier

1. Clique sur **+** (en bas)
2. Sélectionne ta vidé ·o
3. Ajoute une description :

```
Le Ballon Rouge de Lulu 🎈
Histoire pour enfants 1–7 ans
#pourenfants #histoire #kids #french #dessin
```

4. Ajoute une musique douce de la bibliothè·±que TikTok (optionnel)
5. Publie

---

## 5. Straté·±gie de contenu

### Fré·±quence de publication

**YouTube :**
- 2–3 vidé ·os par semaine (ex. lundi, mercredi, vendredi)
- Durée : 30–90 secondes
- Crè·±e des playlists par thè·±me (animaux, jouets, couleurs)

**TikTok :**
- 1 vidé ·o par jour (id é al)
- Durée : 15–60 secondes
- Utilise des hashtags populaires : `#pourenfants`, `#kids`, `#french`

### Idé·±es de sé ·ries

- **"Les Aventures de Lulu"** (lapin curieux)
- **"Couleurs et Jouets"** (dé·±couvertes quotidiennes)
- **"Animaux du Jardin"** (chat, chien, oiseau, etc.)
- **"Histoires du Soir"** (calmes, avant de dormir)

### Engagement

- Réponds aux commentaires (si activé·±s)
- Demande aux parents quels animaux/jouets leurs enfants préfé·±rent
- Crè·±e des vidé ·os bas ées sur les suggestions

---

## 6. Moné·±tisation

### YouTube

**Requis :**
- 1 000 abonné·±s + 4 000 heures de visionnage (ou 10M vues Shorts)

**Revenus :**
- Publicité·±s (AdSense)
- Membres de la chaîne (contenu exclusif)
- Super Thanks / Super Chat (dons)

### TikTok

**Requis :**
- 1 000 abonné·±s (pour le programme de cré ·ateurs)

**Revenus :**
- Programme de ré ·muné·±ration TikTok
- Dons en live
- Partenariats de marques

### Autres

- **Patreon / Ko-fi** : histoires exclusives pour supporters
- **Merch** : peluches, posters des personnages
- **Formations** : "Cré·±er tes propres vidé ·os pour enfants avec IA"

---

## 7. Sécurité et conformité

### COPPA (Children's Online Privacy Protection Act)

- **OUI, destiné aux enfants** : coche cette option sur YouTube
- Pas de collecte de donné ·es personnelles
- Pas de publicit é cibl ée
- Pas de liens vers des sites externes dans les descriptions

### Contenu adapté

- Vérifie chaque vidé ·o avant publication
- Pas de violence, peur, tristesse
- Pas de personnages protégé·±s (Disney, etc.)
- Pas de marques ou logos
- Pas d'appels à l'achat

### Mentions

Ajoute dans tes descriptions :
```
Contenu créé par IA pour les enfants.
Vidè·±os originales et joyeuses, sans violence ni peur.
```

---

## 8. Co ûts indicatifs

Par vidé ·o (30–60 secondes, 4–6 scè·±nes) :

| Poste | Co ût estim é |
|-------|-------------|
| Histoire (LLM) | 0,01–0,03 € |
| Images (DALL‑E 3, 4–6) | 0,12–0,24 € |
| Voix (ElevenLabs, 4–6) | 0,02–0,06 € |
| **Total** | **0,15–0,35 €** |

Pour 30 vidé ·os/mois : ~5–10 €

---

## 9. Prochaines amé·±liorations

- **Musique de fond** : ajoute des tracks libres de droits
- **Sous-titres** : génè·±re des textes coloré·±s automatiquement
- **Text-to-video** : utilise Wan 2.1 ou HunyuanVideo pour des scè·±nes animé·±es
- **Multi-langues** : anglais, espagnol, arabe, etc.
- **Upload auto** : script pour publier automatiquement sur YouTube/TikTok via API

---

## 10. Support

- **Issues GitHub** : https://github.com/ernico1/kids-video-agent/issues
- **Documentation** : https://github.com/ernico1/kids-video-agent

Bon courage pour tes premiè·±res vidé ·os ! 🎈🎨🧸
