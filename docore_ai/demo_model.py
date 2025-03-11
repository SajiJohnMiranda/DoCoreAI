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
    system_message = """
                You are an AI that evaluates a user's request and determines the intelligence profile needed to respond effectively.
                Given a request analyze the content's (both request and response) complexity and predict the required value between the specified range for the intelligence parameters of a person's role to answer 	    this query. The intelligence parameters to be evaluated are reasoning, creativity and precision.
            **Return only the intelligence parameter values** in JSON format:",
            {
                    "reasoning": 0.1 - 1.0,  // How logically structured and in-depth the response should be. 0.1 = simple, 1.0 = deep and complex.
                    "creativity": 0.1 - 1.0, // How much imaginative variation should be introduced. 0.1 = factual, 1.0 = highly creative.
                    "precision": 0.1 - 1.0,  // How specific or general the response should be. 0.1 = broad, 1.0 = highly detailed.
                    "temperature": 0.1 - 1.0, // Derived from above values
            }
            ### **Rules:**                    
            The temperature should be automatically calculated dynamically based on the reasoning, creativity, and precision values.
            Do not provide explanations, only return the JSON output.
    """
    user_message = """
            Analyze the request: {user_content} and understand the complexity of this request and intelligence required for the best possible response.
            Predict the right value between the specified range required for the intelligence parameters of a person's role {role} to answer this query.

            Return them in the structured JSON format:
            {
                "reasoning": 0.1 - 1.0,
                "creativity": 0.1 - 1.0,
                "precision": 0.1 - 1.0,
                "temperature": 0.1 - 1.0
            }
            **Return only the JSON response and no additional text.**
                """
    messages = [
        {"role": "system", "content": "\n".join(system_message)} , #if not manual_mode else None,
        {"role": "user", "content": f'User Input: {user_message}\nRole: Intelligence Evaluator'}
                ]
    messages = [msg for msg in messages if msg]  # Remove None values

    client = Groq(api_key=groq_api_key) 
    chat_completion = client.chat.completions.create(
            messages=messages,
            model="gemma2-9b-it",
            temperature=0.3 # if temperature is not None else (1.0 - reasoning if manual_mode else 0.7)            
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
