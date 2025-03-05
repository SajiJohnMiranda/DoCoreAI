from fastapi import FastAPI
from pydantic import BaseModel
from core_ai.model import optimize_prompt

app = FastAPI(title="CoreAI API", description="Optimize prompts dynamically with reasoning, creativity, and precision.")

class PromptRequest(BaseModel):
    prompt: str
    manual_mode: bool = False  # Flag to enable manual input
    reasoning: float = None
    creativity: float = None
    precision: float = None
    temperature: float = None  # Optional override

@app.post("/optimize-prompt", summary="Optimize a prompt with AI intelligence")
def optimize(request: PromptRequest):
    optimized = optimize_prompt(
        prompt=request.prompt,
        manual_mode=request.manual_mode,
        reasoning=request.reasoning,
        creativity=request.creativity,
        precision=request.precision,
        temperature=request.temperature
    )
    return {"optimized_prompt": optimized}

@app.get("/", summary="Welcome Endpoint")
def home():
    return {"message": "Welcome to CoreAI API. Use /docs for more info."}
