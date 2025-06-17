from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json
import time
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Clothing Analysis API",
    version="1.0.0",
    description="API for clothing analysis using AI"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {
        "message": "Welcome to Clothing Analysis API",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


@app.post("/api/v1/analyze-clothing")
async def analyze_clothing(request_body: dict):
    """
    Analyze a clothing item from an image using AI.
    
    Expected request body:
    {
        "image_base64": "base64_encoded_image_string",
        "additional_info": {}
    }
    """
    start_time = time.time()
    
    try:
        # Validate request
        if not request_body.get("image_base64"):
            raise HTTPException(status_code=400, detail="Image data is required")
        
        # Import OpenAI service
        from app.services.openai_service_simple import analyze_clothing_image
        
        # Analyze the image
        analysis = await analyze_clothing_image(
            request_body["image_base64"],
            request_body.get("additional_info", {})
        )
        
        processing_time = time.time() - start_time
        
        return {
            "success": True,
            "analysis": analysis,
            "processing_time": processing_time
        }
        
    except HTTPException:
        raise
    except Exception as e:
        processing_time = time.time() - start_time
        return {
            "success": False,
            "error": str(e),
            "processing_time": processing_time
        }


@app.get("/api/v1/clothing-categories")
async def get_clothing_categories():
    """Get list of available clothing categories."""
    return {
        "categories": ["top", "bottom", "dress", "outerwear", "shoes", "accessory"]
    }


@app.get("/api/v1/seasons")
async def get_seasons():
    """Get list of available seasons."""
    return {
        "seasons": ["spring", "summer", "autumn", "winter", "all_seasons"]
    }