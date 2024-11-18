# models.py
from pydantic import BaseModel

class RecommendationInput(BaseModel):
    user_input: str  # Adjust the data type as needed
    user_name: str

class RecommendationOutput(BaseModel):
    result: str  # Adjust the data type based on your recommendation system’s output
  
