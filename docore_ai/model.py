import os
from typing import Optional
import openai
import requests
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "groq")  # Choose 'openai' or 'groq'

def intelligence_profiler(user_content: str, role: str, model_provider: str = DEFAULT_MODEL) -> str:
    
    #if manual_mode: # TODO -- manual_mode option can generate efficient prompts based on intelligence params given with input user_content & role 
    #    reasoning = max(0.1, min(1.0, reasoning)) if reasoning is not None else 0.5
    #    creativity = max(0.1, min(1.0, creativity)) if creativity is not None else 0.5
    #    precision = max(0.1, min(1.0, precision)) if precision is not None else 0.5

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
        {"role": "system", "content": "\n".join(system_message)},
        {"role": "user", "content": f'User Input: {user_message}\nRole: Intelligence Evaluator'}

    ]
    messages = [msg for msg in messages if msg]  # Remove None values

    # Choose model provider
    if model_provider == "openai":
        openai.api_key = OPENAI_API_KEY
        response = openai.Client().chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.25
        )
        return response.choices[0].message.content
    elif model_provider == "groq":
        client = Groq(api_key=GROQ_API_KEY) 
        chat_completion = client.chat.completions.create(
            messages=messages,
            model="gemma2-9b-it",
            temperature=0.25 #temperature if temperature is not None else (1.0 - reasoning if manual_mode else 0.7)            
        )       
        response_text = chat_completion.choices[0].message.content  # Extract response
        return response_text