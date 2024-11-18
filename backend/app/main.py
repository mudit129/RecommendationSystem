# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from recommendation import get_recommendation  # Import your recommendation function from recommendation.py
from models import RecommendationInput, RecommendationOutput

app = FastAPI()

@app.get("/{name}")
async def root(name: str):
    return {"msg": "Hello "+name}

@app.post("/recommend", response_model=RecommendationOutput)
async def recommend(input_data: RecommendationInput):
    try:
        # Call the recommendation function with input data
        result = get_recommendation(input_data.user_input, input_data.user_name)
        return RecommendationOutput(result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run the FastAPI server with Uvicorn
# For virtual env - venv\Scripts\activate
# Run using `uvicorn main:app --reload`
# New-Item -Path main.py -ItemType File