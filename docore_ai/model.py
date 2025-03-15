import os
import openai
from groq import Groq
from dotenv import load_dotenv

if not os.path.exists(".env"):
    raise FileNotFoundError("⚠️ Missing .env file! Please create one with API keys. Refer to the README.")

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_PROVIDER = os.getenv("MODEL_PROVIDER")  #'openai' , 'groq' etc
MODEL_NAME = os.getenv("MODEL_NAME")  # gpt-3.5-turbo, gemma2-9b-it 

def intelli_profiler(user_content: str, role: str, model_provider: str = MODEL_PROVIDER, model_name: str = MODEL_NAME) -> str:
    #### LIVE -- LIVE---LIVE -- LIVE
    system_message = f"""
        You are an expert AI assistant. First, analyze the user query and determine optimal intelligence parameters:
        - Reasoning (0.1-1.0): Logical depth
        - Creativity (0.1-1.0): Imagination level
        - Precision (0.1-1.0): Specificity required

        Based on these values, **derive the Temperature dynamically** as follows:
        - If **Precision is high (≥0.8) and Creativity is low (≤0.2)** → **Temperature = 0.1 to 0.3** (Factual & Logical)
        - If **Creativity is high (≥0.8) and Reasoning is low (≤0.3)** → **Temperature = 0.9 to 1.0** (Highly Creative)
        - If **Balanced Creativity & Precision (0.4 - 0.7 range)** → **Temperature = 0.4 to 0.7** (Neutral or Conversational)

        
        You MUST generate responses using the derived temperature value dynamically, ensuring coherence with the intelligence profile.
        Then, generate a response based on these parameters.  

        Return **ONLY** the following JSON format:  
        {{
            "optimized_response": "<AI-generated response>",
            "intelligence_profile": {{ "reasoning": <value>, "creativity": <value>, "precision": <value>, "temperature": <value> # Internally used}}
        }}
    """
    user_message = f"""
    User Request: "{user_content}"
    Role: "{role}"
    """
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message}
    ]

    # Choose model provider
    if model_provider == "openai":
        openai.api_key = OPENAI_API_KEY
        response = openai.Client().chat.completions.create(
            model=model_name,
            messages=messages,
            #temperature=0.3 
        )
        content = response.choices[0].message.content
        usage = response.usage  # Extract token usage
        return {"response": content, "usage": usage}  # Return both content and usage
    elif model_provider == "groq":
        client = Groq(api_key=GROQ_API_KEY) 
        response = client.chat.completions.create(
            messages=messages,
            model=model_name,
            temperature=0.2 
        )       
        content = response.choices[0].message.content  
        usage = response.usage  # Extract token usage
        return {"response": content, "usage": usage}  # Return both content and usage
    
    