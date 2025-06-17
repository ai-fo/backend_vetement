# Guide de démarrage rapide

## 1. Installation

```bash
# Créer l'environnement virtuel
python3 -m venv venv

# Activer l'environnement
source venv/bin/activate  # Sur macOS/Linux
# ou
venv\Scripts\activate  # Sur Windows

# Installer les dépendances
pip install fastapi uvicorn python-multipart python-dotenv openai httpx pillow
```

## 2. Configuration

Assurez-vous que le fichier `.env` contient votre clé API OpenAI :
```
OPENAI_API_KEY=votre_clé_ici
```

## 3. Démarrage du serveur

```bash
# Option 1 : Script simple (recommandé)
python run_simple.py

# Option 2 : Commande directe
uvicorn app.main_simple:app --reload
```

## 4. Accès à l'API

- API : http://localhost:8000
- Documentation interactive : http://localhost:8000/docs

## 5. Test de l'API

Exemple de requête curl :
```bash
curl -X POST "http://localhost:8000/api/v1/analyze-clothing" \
  -H "Content-Type: application/json" \
  -d '{
    "image_base64": "votre_image_base64_ici",
    "additional_info": {}
  }'
```

## Endpoints disponibles

- `POST /api/v1/analyze-clothing` - Analyser une image de vêtement
- `GET /api/v1/clothing-categories` - Liste des catégories
- `GET /api/v1/seasons` - Liste des saisons
- `GET /health` - Vérifier l'état du serveur