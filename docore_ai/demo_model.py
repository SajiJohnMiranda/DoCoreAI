# DEMO --- DEMO --- DEMO --- Works only with Groq
import os
from typing import Optional
import openai
import requests
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "groq")  # demo uses 'groq'



def intelligence_profiler_demo(user_content: str, role: str, reasoning: float = None, 
                    creativity: float = None, precision: float = None, temperature: float = None, 
                    model_provider: str = DEFAULT_MODEL,groq_api_key: str = None
                    ) -> str:

    system_message = f"""
        You are an expert AI assistant. First, analyze the user content and role to determine optimal intelligence parameters required to respond:
        The intelligence parameters are:
        1. Reasoning (0.1-1.0): Logical depth where 1.0 is max value
        2. Creativity (0.1-1.0): Imagination level where 1.0 is max value
        3. Precision (0.1-1.0): Specificity required where 1.0 is max value
        

        Based on these values, **derive the Temperature dynamically** as follows:
        - If **Precision is high (≥0.8) and Creativity is low (≤0.2)** → **Temperature = 0.1 to 0.3** (Factual & Logical)
        - If **Creativity is high (≥0.8) and Reasoning is low (≤0.3)** → **Temperature = 0.9 to 1.0** (Highly Creative)
        - If **Balanced Creativity & Precision (0.4 - 0.7 range)** → **Temperature = 0.4 to 0.7** (Neutral or Conversational)

        
        You MUST generate responses using the derived temperature value dynamically, ensuring coherence with the intelligence profile.
        Then, generate a response based on these parameters.  

        Return **ONLY** the following JSON format:  
        {{
            "intelligence_profile": {{ "reasoning": <value>, "creativity": <value>, "precision": <value>, "temperature": <value> }},
            "optimized_response": "<AI-generated response on {user_content} and your {role}>"
        }}
        Rule: Strictly Do not provide other content or explanations.
    """
    user_message = f"""
    User Request: "{user_content}"
    Role: "{role}"
    """

    messages = [
        {"role": "system", "content": "\n".join(system_message)} , 
        {"role": "user", "content": f'User Input: {user_message}\nRole: Intelligence Evaluator'}
                ]
    messages = [msg for msg in messages if msg]  # Remove None values

    client = Groq(api_key=groq_api_key) 
    chat_completion = client.chat.completions.create(
            messages=messages,
            model="gemma2-9b-it",
            #temperature=1 #DO NOT SET THE TEMPERATURE HERE!
        )       
    response_text = chat_completion.choices[0].message.content  # Extract response
    return response_text

# Custom OpenAPI schema to remove validation errors
'''def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )
    # Remove validation error schemas
    openapi_schema["components"]["schemas"].pop("HTTPValidationError", None)
    openapi_schema["components"]["schemas"].pop("ValidationError", None)
    app.openapi_schema = openapi_schema
    return app.openapi_schema
# Assign the custom OpenAPI schema
app.openapi = custom_openapi'''
