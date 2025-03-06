import os
import openai
import requests
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "groq")  # Choose 'openai' or 'groq'

def optimize_prompt(prompt: str, manual_mode: bool = False, reasoning: float = None, 
                    creativity: float = None, precision: float = None, temperature: float = None, model_provider: str = DEFAULT_MODEL) -> str:
    

    if manual_mode:
        # Ensure provided values are within 0.1 - 1.0 range
        reasoning = max(0.1, min(1.0, reasoning)) if reasoning is not None else 0.5
        creativity = max(0.1, min(1.0, creativity)) if creativity is not None else 0.5
        precision = max(0.1, min(1.0, precision)) if precision is not None else 0.5
    else:
        # System message to let LLM dynamically infer intelligence properties
        system_message = """
        You are an AI that adjusts intelligence dynamically based on user input.
        - Reasoning: Determines logical depth (0.1 = simple, 1.0 = deep).
        - Creativity: Adjusts randomness (0.1 = factual, 1.0 = highly creative).
        - Precision: Controls specificity (0.1 = broad, 1.0 = ultra-specific).
        
        Generate an optimized prompt while self-adjusting these parameters.
        """

    messages = [
        {"role": "system", "content": system_message} if not manual_mode else None,
        {"role": "user", "content": prompt}
    ]
    messages = [msg for msg in messages if msg]  # Remove None values



    # Choose model provider
    if model_provider == "openai":
        openai.api_key = OPENAI_API_KEY
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=messages,
            temperature=temperature if temperature is not None else (1.0 - reasoning if manual_mode else 0.7)
        )
        return response["choices"][0]["message"]["content"]

    elif model_provider == "groq":
       ''' headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "llama-3.1-8b-instant",  # Change based on Groq’s available models
            "messages": messages,
            "temperature": temperature if temperature is not None else (1.0 - reasoning if manual_mode else 0.7)
        }
        response = requests.post("https://api.groq.com/v1/chat/completions", json=data, headers=headers)'''

    client = Groq(api_key=GROQ_API_KEY) # now Groq is used.
   
    chat_completion = client.chat.completions.create(
            messages=messages,
            model="llama-3.1-8b-instant",
            temperature=temperature if temperature is not None else (1.0 - reasoning if manual_mode else 0.7)            
        )       

        
    response_text = chat_completion.choices[0].message.content  # Extract response
    return response_text
