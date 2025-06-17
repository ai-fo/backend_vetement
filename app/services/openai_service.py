import openai
import base64
import json
from typing import Dict, Any
from app.config import get_settings
from app.api.models import ClothingAnalysis, ClothingCategory, Season

settings = get_settings()
openai.api_key = settings.openai_api_key


class OpenAIService:
    def __init__(self):
        self.client = openai.OpenAI(api_key=settings.openai_api_key)
        self.model = settings.openai_model
        
    async def analyze_clothing_image(self, image_base64: str, additional_info: Dict[str, str] = {}) -> ClothingAnalysis:
        try:
            system_prompt = """You are an expert fashion analyst AI. Analyze the clothing item in the image and provide detailed information.
            
            Return a JSON object with the following structure:
            {
                "category": "top/bottom/dress/outerwear/shoes/accessory",
                "colors": ["list of colors"],
                "primary_color": "main color",
                "secondary_colors": ["other colors"],
                "material": "detected material",
                "pattern": "pattern type",
                "style": "style description",
                "season": "spring/summer/autumn/winter/all_seasons",
                "occasion": ["suitable occasions"],
                "care_instructions": "care recommendations",
                "brand": "brand if visible",
                "confidence_score": 0.0-1.0
            }
            
            Be precise and accurate in your analysis."""
            
            user_prompt = "Analyze this clothing item and provide detailed information in JSON format."
            if additional_info:
                user_prompt += f"\nAdditional context: {json.dumps(additional_info)}"
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": user_prompt},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{image_base64}"
                                }
                            }
                        ]
                    }
                ],
                max_tokens=settings.max_tokens,
                temperature=settings.temperature,
                response_format={"type": "json_object"}
            )
            
            result = json.loads(response.choices[0].message.content)
            
            # Map string values to enums
            result['category'] = ClothingCategory(result.get('category', 'top'))
            result['season'] = Season(result.get('season', 'all_seasons'))
            
            return ClothingAnalysis(**result)
            
        except Exception as e:
            print(f"Error analyzing image: {str(e)}")
            raise


openai_service = OpenAIService()