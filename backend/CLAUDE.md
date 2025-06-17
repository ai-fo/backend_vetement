# Backend Application - Analyse d'Images de Vêtements

## Vue d'ensemble
Backend Python pour l'analyse et les conseils d'images de vêtements utilisant ChatGPT-4o.

## Architecture

### Structure du projet
```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Point d'entrée FastAPI
│   ├── config.py               # Configuration et variables d'environnement
│   ├── agents/                 # Agents IA
│   │   ├── __init__.py
│   │   ├── base_agent.py       # Classe de base pour les agents
│   │   ├── image_analyzer.py   # Agent d'analyse d'images
│   │   ├── style_advisor.py    # Agent de conseils de style
│   │   └── orchestrator.py     # Orchestrateur multi-agents
│   ├── services/               # Services métier
│   │   ├── __init__.py
│   │   ├── openai_service.py   # Interface avec OpenAI API
│   │   └── image_service.py    # Traitement d'images
│   ├── api/                    # Endpoints API
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── models.py           # Modèles Pydantic
│   └── utils/                  # Utilitaires
│       ├── __init__.py
│       └── helpers.py
├── tests/                      # Tests unitaires et d'intégration
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Stack technique
- **Framework**: FastAPI
- **IA**: OpenAI GPT-4o API
- **Base de données**: PostgreSQL (si nécessaire)
- **Cache**: Redis (pour optimiser les appels API)
- **Tests**: pytest
- **Linting**: black, flake8
- **Type checking**: mypy

## Workflow de développement

### Branches
- `main`: Production
- `develop`: Développement
- `feature/*`: Nouvelles fonctionnalités
- `fix/*`: Corrections de bugs

### Process pour chaque fonctionnalité
1. Créer une branche feature depuis develop
2. Développer et tester localement
3. Push et créer une PR vers develop
4. Tests automatiques et review
5. Merge dans develop
6. Quand stable, merge develop → main

## Fonctionnalités principales

### 1. Analyse d'images
- Détection des vêtements
- Identification des couleurs
- Reconnaissance des styles
- Analyse de la qualité

### 2. Conseils personnalisés
- Recommandations de style
- Suggestions de combinaisons
- Conseils selon la morphologie
- Adaptations selon les occasions

### 3. Collaboration multi-agents
- Agent d'analyse visuelle
- Agent de conseil mode
- Agent de personnalisation
- Orchestrateur central

## Configuration des agents

### Structure d'un agent
```python
class BaseAgent:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        self.memory = []
    
    async def process(self, input_data: dict) -> dict:
        # Logique de traitement
        pass
    
    async def collaborate(self, other_agent: 'BaseAgent', data: dict) -> dict:
        # Logique de collaboration
        pass
```

## Variables d'environnement
```
OPENAI_API_KEY=your_key_here
REDIS_URL=redis://localhost:6379
DATABASE_URL=postgresql://user:password@localhost/dbname
```

## Commandes utiles
- `pip install -r requirements.txt` - Installer les dépendances
- `uvicorn app.main:app --reload` - Lancer le serveur de développement
- `pytest` - Lancer les tests
- `black .` - Formater le code
- `flake8` - Vérifier le style
- `mypy app/` - Vérifier les types

## Endpoints API principaux
- `POST /analyze-image` - Analyser une image de vêtement
- `POST /get-style-advice` - Obtenir des conseils de style
- `GET /analysis-history` - Historique des analyses
- `POST /combine-outfits` - Suggérer des combinaisons

## Gestion des erreurs
- Validation des entrées avec Pydantic
- Gestion des limites de taux pour l'API OpenAI
- Retry automatique en cas d'échec
- Logging détaillé pour le debugging