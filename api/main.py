from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from docore_ai.model import intelli_profiler
from docore_ai.demo_model import intelligence_profiler_demo
from fastapi import Header

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api.main:app", host="127.0.0.1", port=8000, reload=True)

app = FastAPI(
    title="DoCoreAI API",
    description="""🚀 Elevate Your AI’s Intelligence with Contextually Smart Responses!  
The DoCoreAI API analyzes prompts and **profiles the intelligence parameters** required to generate effective responses.  
By optimizing reasoning, creativity, and precision, it ensures that **AI-driven applications produce more relevant, insightful, and impactful outputs**.  

💡 **Why Use DoCoreAI's Intelligence Profiler?**  
✅ **Unlock AI Intelligence** – Get structured intelligence parameters for optimized responses.  
✅ **Seamless LLM Integration** – Works effortlessly with OpenAI, Groq, Anthropic, Mistral, and more.  
✅ **Optimized for Agentic AI** – Enhance decision-making in autonomous AI workflows.  
✅ **Developer-Friendly & Scalable** – FastAPI-powered, efficient, and easy to integrate.""",    version="1.0"
)

class PromptRequest(BaseModel):
    user_content: str = Field(..., example="Can you help me to connect my laptop to wifi?")
    role: str = Field(None, example="Technical Support Agent", description="Role of LLM")

@app.get("/", summary="Welcome to CoreAI Endpoint")
def home():
    return {"message": "Welcome to CoreAI API. Use /docs for more info."}

@app.post("/intelli_profiler", summary="Give a prompt with intelligence paramters",  include_in_schema=False)
def prompt_live_intelli_profiler(request: PromptRequest):

    optimal_response = intelli_profiler(
        user_content=request.user_content,
        role=request.role,
    )
    return {"optimal_response":optimal_response}


class DemoPromptRequest(BaseModel):
    user_content: str = Field(..., example="Can you walk me through how to connect my laptop to this new network?")
    #manual_mode: bool = Field(False, example=False, description="Enable manual input mode")
    role: str = Field(None, example="Technical Support Agent", description="Role of LLM")

@app.post("/intelligence-profiler-demo", summary="""🎯 Optimize Your Prompts for Smarter AI Responses!
This endpoint enhances standard prompts by dynamically injecting reasoning, creativity, and precision, making them more effective for LLMs and Agentic AI applications.""")
def intelligence_profiler_swagger_demo(request: DemoPromptRequest, groq_api_key: str = Header(None, description="Groq API Token")):
        """
        This endpoint enhances a given prompt with AI intelligence properties 
        such as reasoning, creativity, and precision.

        - **user_content**: The original input text.
        - **role**: The role or designation of the Agent.
        - **reasoning**: Logical depth (higher means more detailed reasoning).
        - **creativity**: Adjusts randomness and freeform nature of the response.
        - **precision**: Determines specificity (higher means more detailed responses).
        - **temperature**: Controls variability in AI-generated text.

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
            "temperature": 0.7,
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
