import openai
import json
import os
from typing import Dict, Any

# Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4-vision-preview")
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "1000"))
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))

# Initialize OpenAI client
client = openai.OpenAI(api_key=OPENAI_API_KEY)


async def analyze_clothing_image(image_base64: str, additional_info: Dict[str, str] = {}) -> Dict[str, Any]:
    """
    Analyze a clothing image using OpenAI's GPT-4 Vision
    """
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
        
        response = client.chat.completions.create(
            model=OPENAI_MODEL,
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
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE,
            response_format={"type": "json_object"}
        )
        
        result = json.loads(response.choices[0].message.content)
        
        # Ensure all required fields are present
        result.setdefault('category', 'top')
        result.setdefault('colors', [])
        result.setdefault('primary_color', 'unknown')
        result.setdefault('secondary_colors', [])
        result.setdefault('season', 'all_seasons')
        result.setdefault('confidence_score', 0.95)
        
        return result
        
    except Exception as e:
        print(f"Error analyzing image: {str(e)}")
        raise