# This file needs to be deleted later as we will be relying on api\main.py

from fastapi import FastAPI
from pydantic import BaseModel, Field
from core_ai.model import optimize_prompt

app = FastAPI(
    title="CoreAI API",
    description="Optimize prompts dynamically with AI intelligence properties like reasoning, creativity, and precision.",
    version="1.0"
)


class PromptRequest(BaseModel):
    prompt: str = Field(..., example="How can AI improve healthcare?")
    manual_mode: bool = Field(False, example=False, description="Enable manual input mode")
    reasoning: float = Field(0.7, example=0.7, description="Logical depth (0.1 = simple, 1.0 = deep)")
    creativity: float = Field(0.6, example=0.6, description="Randomness level (0.1 = strict, 1.0 = freeform)")
    precision: float = Field(0.8, example=0.8, description="Specificity (0.1 = vague, 1.0 = ultra-detailed)")
    temperature: float = Field(None, example=0.7, description="Optional override for AI temperature")    

@app.post("/optimize-prompt", summary="Optimize a prompt with AI intelligence")
def optimize(request: PromptRequest):
    """
    Optimizes a given prompt by adjusting reasoning, creativity, and precision levels dynamically.
    
    - **manual_mode**: If true, lets the user manually control reasoning, creativity, precision.
    - **reasoning**: Adjusts logical depth (0.1 = simple, 1.0 = deep).
    - **creativity**: Controls randomness (0.1 = strict, 1.0 = freeform).
    - **precision**: Determines specificity (0.1 = vague, 1.0 = ultra-detailed).
    - **temperature**: Optional override for AI's temperature.
    Example Input:
    ```json
    {
        "prompt": "How can AI improve healthcare?",
        "manual_mode": false,
        "reasoning": 0.7,
        "creativity": 0.6,
        "precision": 0.8
    }
    ```
    """      

@app.get("/", summary="Welcome to CoreAI Endpoint")
def home():
    return {"message": "Welcome to CoreAI API. Use /docs for more info."}

@app.post("/optimize-prompt")
def optimize_prompt_endpoint(request: PromptRequest):
    return {"optimized_prompt": f"Optimized: {request.prompt}"}


