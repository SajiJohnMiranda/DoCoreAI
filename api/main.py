from fastapi import FastAPI
from pydantic import BaseModel, Field
#from core_ai.model import optimize_prompt

app = FastAPI(
    title="CoreAI API",
    description="""🚀 Empower Your AI Agents with Contextually Smart Prompts! 
CoreAI API transforms ordinary prompts into intelligent, context-aware queries infused with reasoning, creativity, and precision.
With finely-tuned prompts, developers can build LLM-powered applications, autonomous AI agents, and smarter decision-making systems.

💡 Why Use CoreAI API?
✅ Enhance Prompt Intelligence – Get better AI-generated responses across LLMs.
✅ Plug & Play with Any LLM – Works seamlessly with OpenAI, Anthropic, Mistral, etc.
✅ Optimized for Agentic AI – Enable smarter decision-making in AI-driven workflows.
✅ Developer-Friendly & Scalable – FastAPI-powered, blazing-fast, and easy to integrate.""",
    version="1.0"
)


class PromptRequest(BaseModel):
    prompt: str = Field(..., example="Can you walk me through how to connect my laptop to this new network?")
    manual_mode: bool = Field(False, example=False, description="Enable manual input mode")
    role: bool = Field(None, example="Technical Support Executive", description="Role of LLM")
    #reasoning: float = Field(0.7, example=0.7, description="Logical depth (0.1 = simple, 1.0 = deep)")
    #creativity: float = Field(0.6, example=0.6, description="Randomness level (0.1 = strict, 1.0 = freeform)")
    #precision: float = Field(0.8, example=0.8, description="Specificity (0.1 = vague, 1.0 = ultra-detailed)")
    #temperature: float = Field(None, example=0.7, description="Optional override for AI temperature")    


@app.get("/", summary="Welcome to CoreAI Endpoint")
def home():
    return {"message": "Welcome to CoreAI API. Use /docs for more info."}

@app.post("/optimize-prompt", summary="""🎯 Transform Standard Prompts into AI-Optimized Queries for Smarter Responses!
This endpoint dynamically enhances prompts by injecting reasoning, creativity, and precision, making them more effective for LLMs and Agentic AI applications.""")
def optimize_prompt_endpoint(request: PromptRequest):
        """
        This endpoint enhances a given prompt with AI intelligence properties 
        such as reasoning, creativity, and precision.

        - **prompt**: The original input text.
        - **manual_mode**: Enables manual input adjustments.
        - **reasoning**: Logical depth (higher means more detailed reasoning).
        - **creativity**: Adjusts randomness and freeform nature of the response.
        - **precision**: Determines specificity (higher means more detailed responses).
        - **temperature**: Controls variability in AI-generated text.

        **Example Input:**
        ```json
        {
            "prompt": "Can you walk me through how to connect my laptop to this new network?",
            "manual_mode": false
        }
        ```

        **Example Response:**
        ```json
        {
            "prompt": "Can you walk me through how to connect my laptop to this new network?",
            "reasoning": 0.7,
            "creativity": 0.6,
            "precision": 0.8,
            "temperature": 0.7
        }
        ```
        """
        return {
            "prompt": request.prompt,
            "reasoning": 0.7,
            "creativity": 0.6,
            "precision": 0.8,
            "temperature": 0.7
        }


'''from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to CoreAI! - main.py"}'''
