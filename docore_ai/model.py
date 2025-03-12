import os
from typing import Optional
import openai
import requests
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "groq")  # Default to groq
MODEL = os.getenv("MODEL", "gemma2-9b-it")  # Default to gemma2-9b-it


def intelligence_profiler(user_content: str, role: str, model_provider: str = DEFAULT_MODEL, model_name: str = MODEL) -> str:
    
    #if manual_mode: # TODO -- manual_mode option can generate efficient prompts based on intelligence params given with input user_content & role 
    #    reasoning = max(0.1, min(1.0, reasoning)) if reasoning is not None else 0.5
    #    creativity = max(0.1, min(1.0, creativity)) if creativity is not None else 0.5
    #    precision = max(0.1, min(1.0, precision)) if precision is not None else 0.5

    system_message = """
    You are an AI Intelligence Profiler. Your task is to analyze a user's request and determine the optimal intelligence parameters needed for an effective response. The parameters to be evaluated are:

    - **reasoning** (0.1 to 1.0): The level of logical depth required.
    - **creativity** (0.1 to 1.0): The degree of imaginative variation required.
    - **precision** (0.1 to 1.0): The specificity level required.
    - **temperature** (0.1 to 1.0): A value derived from the above parameters that influences overall output variability.

    **Instructions:**
    1. Analyze the user's request and consider the specified role.
    2. Adjust the intelligence parameters based on the query's complexity and the typical expertise required for that role.
    3. **Return ONLY a JSON object** in the exact format below, with no extra text or explanation:

    {
        "reasoning": <value>,
        "creativity": <value>,
        "precision": <value>,
        "temperature": <value>
    }
    """
    user_message = f"""
    User Request: "{user_content}"
    Role: "{role}"
   

    Please evaluate the above information and return the intelligence parameters in the specified JSON format.
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
            temperature=0.4
        )
        return response.choices[0].message.content
    elif model_provider == "groq":
        client = Groq(api_key=GROQ_API_KEY) 
        chat_completion = client.chat.completions.create(
            messages=messages,
            model=model_name,
            temperature=0.2 #temperature if temperature is not None else (1.0 - reasoning if manual_mode else 0.7)            
        )       
        response_text = chat_completion.choices[0].message.content  # Extract response
        return response_text
    
def normal_prompt(user_content: str, role: str, model_provider: str = DEFAULT_MODEL, model_name: str = MODEL):
    """
    Sends a normal prompt to the selected LLM (OpenAI or Groq) without intelligence parameters.
    """
    system_message = f"""
    You are a {role}. Respond to user queries based on your role expertise.
    Provide a well-structured response based on best practices in your field.
    """

    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_content}
    ]

    response = call_llm_without_temp(model_provider, model_name, messages)
    return response

def normal_prompt_with_intelligence(user_content: str, role: str, model_provider: str = DEFAULT_MODEL, model_name: str = MODEL, reasoning: float = 0.5, creativity: float = 0.5, precision: float = 0.5, temperature: float = 0.5):
    """
    Sends a prompt to the selected LLM with intelligence parameters.
    """
    system_message = f"""
    You are a {role}. Respond to user queries based on your role expertise.
    Provide a well-structured response based on best practices in your field.
    Adjust the response style dynamically based on intelligence parameters:
    - Reasoning: {reasoning} (0.1 = simple, 1.0 = deep and structured)
    - Creativity: {creativity} (0.1 = factual, 1.0 = imaginative)
    - Precision: {precision} (0.1 = broad, 1.0 = highly detailed)
    """

    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_content}
    ]

    response = call_llm(model_provider, model_name, messages, temperature)
    return response

def call_llm(model_provider: str, model_name: str, messages: list, temperature: float):
    """
    Handles communication with OpenAI or Groq models.
    """
    if model_provider == "openai":
        response = openai.Client().chat.completions.create(
            model=model_name,
            messages=messages,
            temperature=temperature
        )
        return response.choices[0].message.content

    elif model_provider == "groq":
        # Implement Groq API call (replace with actual implementation)
        client = Groq(api_key=GROQ_API_KEY) 
        chat_completion = client.chat.completions.create(
            messages=messages,
            model=model_name,
            temperature=temperature #temperature if temperature is not None else (1.0 - reasoning if manual_mode else 0.7)            
        )
        return f"Simulated Groq response for model: {model_name}, Temp: {temperature}"

    else:
        raise ValueError("Invalid model provider. Choose 'openai' or 'groq'.")

def call_llm_without_temp(model_provider: str, model_name: str, messages: list):
    """
    Calls OpenAI or Groq API without specifying temperature, so it defaults to the model's own value.
    """
    if model_provider == "openai":
        response = openai.Client().chat.completions.create(
            model=model_name,
            messages=messages
        )
        return response.choices[0].message.content

    elif model_provider == "groq":
        client = Groq(api_key=GROQ_API_KEY) 
        chat_completion = client.chat.completions.create(
            messages=messages,
            model=model_name,
        )
        return f"Simulated Groq response for model: {model_name} (Using default LLM temperature)"

    else:
        raise ValueError("Invalid model provider. Choose 'openai' or 'groq'.")
