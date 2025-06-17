from pydantic import BaseModel
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
    colors: List[str]
    primary_color: str
    secondary_colors: List[str] = []
    material: Optional[str] = None
    pattern: Optional[str] = None
    style: Optional[str] = None
    season: Season
    occasion: List[str] = []
    care_instructions: Optional[str] = None
    brand: Optional[str] = None
    confidence_score: float


class AnalyzeClothingRequest(BaseModel):
    image_base64: str
    additional_info: Optional[Dict[str, str]] = {}


class AnalyzeClothingResponse(BaseModel):
    success: bool
    analysis: Optional[ClothingAnalysis] = None
    error: Optional[str] = None
    processing_time: float