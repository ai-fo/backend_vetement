from fastapi import APIRouter, HTTPException
from app.api.models import AnalyzeClothingRequest, AnalyzeClothingResponse
from app.services.openai_service import openai_service
import time

router = APIRouter()


@router.post("/analyze-clothing", response_model=AnalyzeClothingResponse)
async def analyze_clothing(request: AnalyzeClothingRequest):
    """
    Analyze a clothing item from an image using AI.
    
    The image should be provided as a base64 encoded string.
    """
    start_time = time.time()
    
    try:
        # Validate base64 image
        if not request.image_base64:
            raise HTTPException(status_code=400, detail="Image data is required")
        
        # Analyze the image
        analysis = await openai_service.analyze_clothing_image(
            request.image_base64,
            request.additional_info
        )
        
        processing_time = time.time() - start_time
        
        return AnalyzeClothingResponse(
            success=True,
            analysis=analysis,
            processing_time=processing_time
        )
        
    except HTTPException:
        raise
    except Exception as e:
        processing_time = time.time() - start_time
        return AnalyzeClothingResponse(
            success=False,
            error=str(e),
            processing_time=processing_time
        )


@router.get("/clothing-categories")
async def get_clothing_categories():
    """Get list of available clothing categories."""
    from app.api.models import ClothingCategory
    return {
        "categories": [category.value for category in ClothingCategory]
    }


@router.get("/seasons")
async def get_seasons():
    """Get list of available seasons."""
    from app.api.models import Season
    return {
        "seasons": [season.value for season in Season]
    }