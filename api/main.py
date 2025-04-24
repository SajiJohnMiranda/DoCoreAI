from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from docore_ai.model import intelligence_profiler, normal_prompt
from docore_ai.demo_model import intelligence_profiler_demo
from fastapi import Header

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api.main:app", host="127.0.0.1", port=8000, reload=True)

app = FastAPI(
    title="DoCoreAI: Smarter AI Responses with Automated Intelligence Profiling",
    description="""🚀 The DoCoreAI API analyzes prompts, determines intelligence parameters, and optimizes response generation. By fine-tuning reasoning, creativity, precision, and temperature, it helps AI models produce more relevant and structured outputs.  

💡 **Why Use DoCoreAI**  

✔ **Analyzes query complexity** – Understands the intent and adjusts the Intelligence accordingly.  
✔ **Enhances AI responses** – Dynamically applies reasoning, creativity, and precision.  
✔ **Role-based adaptability** – Adjusts responses based on expertise (e.g., tech support, maths-teacher, artist etc).  
✔ **Optimal content structuring** – Automatically determines the best response format.  
✔ **Auto temperature tuning** – No need to manually tweak temperature values; Eliminates manual adjustments by predicting the best value.  
✔ **Efficient and cost-effective** – Saves tokens by optimizing response generation.  
✔ **Developer-friendly** – No more trial-and-error tuning—just integrate and get optimized results instantly.

🔗**Compatible with:** OpenAI, Groq, Anthropic, Mistral, and more. ⚡**FastAPI-powered** – Built for speed and scalability. 🚀
""",    version="1.0"
)

class PromptRequest(BaseModel):
    user_content: str = Field(..., example="Can you help me to connect my laptop to wifi?")
    role: str = Field(None, example="Technical Support Agent", description="Role of LLM")

@app.get("/", summary="Welcome to CoreAI Endpoint")
def home():
    return {"message": "Welcome to CoreAI API. Use /docs for more info."}

@app.post("/intelligence_profiler", summary="Give a prompt with intelligence paramters",  include_in_schema=False)
def prompt_live_intelli_profiler(request: PromptRequest):

    optimal_response = intelligence_profiler(
        user_content=request.user_content,
        role=request.role,
    )
    return {"optimal_response":optimal_response}


@app.post("/normal_prompt", summary="For testing purpose only",  include_in_schema=False)
def normal_prompt_live(request: PromptRequest):

    normal_prompt_response = normal_prompt(
        user_content=request.user_content,
        role=request.role
    )
    return {"normal_response":normal_prompt_response}


class PromptRequestAdvanced(BaseModel):
    user_content: str
    role: Optional[str] = None
    model_provider: Optional[str] = "openai"
    model_name: Optional[str] = "gpt-3.5-turbo"
    show_token_usage: Optional[bool] = True
    token: Optional[str] = None
@app.post("/intelligence_profiler_advanced", summary="Advanced profiling with manual token")
def prompt_live_intelli_profiler_advanced(request: PromptRequestAdvanced):
    
    optimal_response = intelligence_profiler(
        user_content=request.user_content,
        role=request.role,
        model_provider=request.model_provider,
        model_name=request.model_name,
        show_token_usage=request.show_token_usage,
        token=request.token  # new!
    )
    return {"optimal_response": optimal_response}


class DemoPromptRequest(BaseModel):
    user_content: str = Field(..., example="Can you walk me through how to connect my laptop to this new network?")
    #manual_mode: bool = Field(False, example=False, description="Enable manual input mode")
    role: str = Field(None, example="Technical Support Agent", description="Role of LLM")

@app.post("/intelligence-profiler-demo", summary="""🎯 Optimize your prompts for Smarter AI responses 
with dynamically injected reasoning, creativity & precision params that boosts your LLM's intelligence.""")
def intelligence_profiler_swagger_demo(request: DemoPromptRequest, groq_api_key: str = Header(None, description="Groq API Token")):
        """
        This endpoint enhances a given prompt with AI intelligence properties 
        such as reasoning, creativity, and precision.

        - **user_content**: The original input text.
        - **role**: The role or designation of the Agent.
        - **reasoning**: Logical depth (higher means more detailed reasoning).
        - **creativity**: Adjusts randomness and freeform nature of the response.
        - **precision**: Determines specificity (higher means more detailed responses).
        - **temperature**: Controls variability/randomness in AI-generated text.

        **Example Input:**
        ```json
        {
            "user_content": "Can you walk me through how to connect my laptop to this new network?",
            "role": "Technical Support Agent",
        }
        ```

        **Example Response:**
        ```json
        {
            "Response" : "Sure! Right click on the icon that displays network, and then.....",
            "reasoning": 0.7,
            "creativity": 0.6,
            "precision": 0.8,
            "temperature": 0.7
        }        
        ```

        ### **What’s Happening Here?**  
        - The **LLM evaluates the complexity** of the query {user_content} and determines the optimal intelligence parameters needed for the best response.  

        ### **Why Is This Useful for AI Projects?**  
        - When **{user_content}** is combined with the **calibrated intelligence parameters**, the prompt becomes significantly more effective.  
        - AI models will **generate more precise, context-aware, and useful responses** instead of generic answers.  
        - This approach **reduces hallucination** and improves AI-driven decision-making in real-world applications.  

        **How to Use:**
        - Enter the Groq API token in the "Authorize" section.
        - Input request parameters in the request body.
        - Click "Try it Out" to test.

        ### **🚀 Ready to See It in Action?**  
        ✅ **Fork the repo** and start experimenting instantly!  
        ✅ **Try the live API** and witness how AI intelligence optimization works in real time.  
        🔗 *https://github.com/SajiJohnMiranda/DoCoreAI* 

        """
        if not groq_api_key:
            raise HTTPException(status_code=400, detail="Groq API Token is required for demo mode.")

        optimized_prompt = intelligence_profiler_demo(
            user_content=request.user_content,
            #manual_mode=False,
            role=request.role,
            model_provider="groq",  
            groq_api_key =groq_api_key
            #temperature=0.3  # Keep default demo temperature                       
        )


        return {"intelligence_profile": optimized_prompt,
                "model_provider": "groq",
                "groq_token_received": bool(groq_api_key)  # Confirm token received
        }
        

#@app.get("/live", summary="Health Check Endpoint")
#def health_check():
#    return {"status": "running"}
