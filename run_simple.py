#!/usr/bin/env python3
"""
Script de démarrage pour la version simplifiée sans Pydantic
"""
import sys
import os

# Ajouter le répertoire actuel au path Python
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import uvicorn
from app.main_simple import app

if __name__ == "__main__":
    print("Starting Clothing Analysis API (Simple Version)...")
    print("API Documentation will be available at: http://localhost:8000/docs")
    print("\nMake sure you have set OPENAI_API_KEY in your .env file")
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)