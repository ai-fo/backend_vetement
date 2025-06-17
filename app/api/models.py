from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from enum import Enum


class Season(str, Enum):
    SPRING = "spring"
    SUMMER = "summer"
    AUTUMN = "autumn"
    WINTER = "winter"
    ALL_SEASONS = "all_seasons"


class ClothingCategory(str, Enum):
    TOP = "top"
    BOTTOM = "bottom"
    DRESS = "dress"
    OUTERWEAR = "outerwear"
    SHOES = "shoes"
    ACCESSORY = "accessory"


class ClothingAnalysis(BaseModel):
    category: ClothingCategory
    colors: List[str] = Field(..., description="List of main colors detected")
    primary_color: str = Field(..., description="The dominant color")
    secondary_colors: List[str] = Field(default=[], description="Other colors present")
    material: Optional[str] = Field(None, description="Detected material type")
    pattern: Optional[str] = Field(None, description="Pattern type (solid, striped, etc.)")
    style: Optional[str] = Field(None, description="Style description")
    season: Season = Field(..., description="Recommended season(s)")
    occasion: List[str] = Field(default=[], description="Suitable occasions")
    care_instructions: Optional[str] = Field(None, description="Care recommendations")
    brand: Optional[str] = Field(None, description="Brand if visible")
    confidence_score: float = Field(..., ge=0, le=1, description="Analysis confidence")


class AnalyzeClothingRequest(BaseModel):
    image_base64: str = Field(..., description="Base64 encoded image")
    additional_info: Optional[Dict[str, str]] = Field(default={}, description="Additional context")


class AnalyzeClothingResponse(BaseModel):
    success: bool
    analysis: Optional[ClothingAnalysis] = None
    error: Optional[str] = None
    processing_time: float = Field(..., description="Processing time in seconds")