# Démarrage ultra-rapide (5 minutes)

## Étape 1 – Obtenir les clés API (2 min)

### OpenAI
1. Va sur https://platform.openai.com/api-keys
2. Clique sur **Create new secret key**
3. Copie la clé (commence par `sk-...`)

### ElevenLabs
1. Va sur https://elevenlabs.io
2. Clique sur ton profil → **API Keys**
3. Copie la clé API

---

## Étape 2 – Ajouter les secrets GitHub (2 min)

1. Va sur https://github.com/ernico1/kids-video-agent/settings/secrets/actions
2. Clique sur **New repository secret**
3. Ajoute les 3 secrets :

| Nom | Valeur |
|-----|--------|
| `OPENAI_API_KEY` | `sk-...` (ta clé OpenAI) |
| `ELEVENLABS_API_KEY` | Ta clé ElevenLabs |
| `ELEVENLABS_VOICE_ID` | `Rachel` (ou autre voix) |

4. Clique sur **Add secret** pour chaque

---

## Étape 3 – Lancer la première vidéo (1 min)

1. Va sur https://github.com/ernico1/kids-video-agent/actions
2. Clique sur **Generate Kids Video**
3. Clique sur **Run workflow** (bouton vert)
4. Attends 5–10 minutes

---

## Étape 4 – Télécharger la vidéo

1. Clique sur le workflow en cours (ex. "Generate Kids Video #1")
2. Attends que tous les checks soient verts ✅
3. Descends en bas de page → section **Artifacts**
4. Clique sur **kids-video** pour télécharger le MP4

---

## ✅ Checklist de validation

- [ ] Clé·±s API obtenues (OpenAI + ElevenLabs)
- [ ] Secrets GitHub ajout é s
- [ ] Workflow lancé manuellement
- [ ] Vidéo téléchargé·±e et vérifié·±e

---

## 🎯 Prochaine étape

Publie ta premiè·±re vidé ·o sur :

- **YouTube** : https://youtube.com/upload
- **TikTok** : https://tiktok.com/upload

Utilise les titres et descriptions du fichier `CALENDRIER_30_JOURS.md`.

---

## 🆘 Problè·±mes fréquents

### Workflow en échec ❌
- Vérifie que les secrets sont bien ajout é s
- Vérifie que les clés API sont valides
- Regarde les logs du workflow (clique sur chaque étape)

### Vidéo trop longue
- Modifie `agent_config.yaml` → `target_duration_max: 60`

### Co ûts trop é lev é s
- Réduis le nombre de scè·±nes : `scenes_max: 4`

---

## 📞 Besoin d'aide ?

- **Issues GitHub** : https://github.com/ernico1/kids-video-agent/issues
- **Documentation complè·±te** : `README.md`, `SETUP_GUIDE.md`
