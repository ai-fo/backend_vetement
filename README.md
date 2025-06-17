# Clothing Analysis Backend

Backend API for clothing analysis using OpenAI GPT-4 Vision.

## Features

- Analyze clothing images to extract:
  - Category (top, bottom, dress, etc.)
  - Colors (primary and secondary)
  - Material
  - Pattern
  - Style
  - Recommended season
  - Suitable occasions
  - Care instructions
  - Brand (if visible)

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Copy `.env.example` to `.env` and add your OpenAI API key:
```bash
cp .env.example .env
```

4. Run the server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Visit `http://localhost:8000/docs` for interactive API documentation.

### Main Endpoints

- `POST /api/v1/analyze-clothing` - Analyze a clothing item from an image
- `GET /api/v1/clothing-categories` - Get list of clothing categories
- `GET /api/v1/seasons` - Get list of seasons

### Example Request

```json
POST /api/v1/analyze-clothing
{
  "image_base64": "base64_encoded_image_string",
  "additional_info": {
    "user_preference": "casual style"
  }
}
```

### Example Response

```json
{
  "success": true,
  "analysis": {
    "category": "top",
    "colors": ["blue", "white"],
    "primary_color": "blue",
    "secondary_colors": ["white"],
    "material": "cotton",
    "pattern": "striped",
    "style": "casual t-shirt",
    "season": "summer",
    "occasion": ["casual", "everyday"],
    "care_instructions": "Machine wash cold",
    "brand": null,
    "confidence_score": 0.95
  },
  "processing_time": 1.23
}
```

## Development

- Format code: `black .`
- Lint: `flake8`
- Type check: `mypy app/`
- Run tests: `pytest`