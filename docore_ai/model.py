import os
#import sys
from typing import Optional
import openai
from groq import Groq
from research.Telm.jsonbin import update_jsonbin, is_telemetry_enabled
from dotenv import load_dotenv
import threading

if is_telemetry_enabled():
    thread = threading.Thread(target=update_jsonbin, args=("Upgrade",))
    thread.daemon = True  # Allows the program to exit even if telemetry is still running
    thread.start()

if not os.path.exists(".env"):
    raise FileNotFoundError("⚠️ Missing .env file! Please create one with API keys. Refer to the README https://github.com/SajiJohnMiranda/DoCoreAI/.")

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_PROVIDER = os.getenv("MODEL_PROVIDER")  #'openai' , 'groq' etc
MODEL_NAME = os.getenv("MODEL_NAME")  # gpt-3.5-turbo, gemma2-9b-it 

def intelligence_profiler(user_content: str, role: str, model_provider: str = MODEL_PROVIDER, model_name: str = MODEL_NAME,
                          show_token_usage: Optional[bool] = False) -> dict:
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
        - If **Reasoning is high (≥0.8) and Creativity is moderate (0.4-0.7)** → **Temperature = 0.3 to 0.5** (Logical with slight abstraction)
        - If **Precision is high (≥0.8) and Reasoning is low (≤0.3)** → **Temperature = 0.2 to 0.3** (Fact-driven, minimal context)
        - If **Reasoning, Creativity, and Precision are all high (≥0.8)** → **Temperature = 0.6 to 0.9** (Balanced, intelligent, and flexible)

        
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
            #temperature=0.7 # Default - TEMPERATURE SETTING NOT REQUIRED!
        )
        content = response.choices[0].message.content
        usage = response.usage  # Extract token usage


        if show_token_usage:
            return {"response": content, "usage": usage}  # Return both content and usage
        else:
            return {"response": content}

    elif model_provider == "groq":
        client = Groq(api_key=GROQ_API_KEY) 

        # Append new user query to message history -MEMORY WIP ToDO
        #messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            messages=messages,
            model=model_name,
            #temperature=0 #TEMPERATURE SETTING NOT REQUIRED - for Intelligence Profiler Prompt
        )       
        content = response.choices[0].message.content  
        usage = response.usage  # Extract token usage

        # Append AI response to message history -MEMORY WIP ToDO
        #messages.append({"role": "assistant", "content": content})        

        if show_token_usage:
            return {"response": content, "usage": usage}  # Return both content and usage
        else:
            return {"response": content}
    
#Added only for tetsting
def normal_prompt(user_content: str, role: str, model_provider: str = MODEL_PROVIDER, model_name: str = MODEL_NAME, 
                  show_token_usage: Optional[bool] = False) -> dict:
    """  Sends a normal prompt to the selected LLM (OpenAI or Groq) without intelligence parameters.
    """
    system_message = f"""
    You are an AI assistant. Your goal is to respond to user queries as accurately as possible.

    - Generate a **coherent and informative** response based on the user's request.
    - Ensure responses remain relevant to the given context.

    Return **ONLY** the following JSON format:  
    {{
        "response": "<AI-generated response>"
    }}
    """
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_content}
    ]
    # Choose model provider
    if model_provider == "openai":
        openai.api_key = OPENAI_API_KEY
        response = openai.Client().chat.completions.create(
            model=model_name,
            messages=messages,
            temperature=0.8 # Default - TEMPERATURE SETTING - for Normal Prompt

        )
        content = response.choices[0].message.content
        usage = response.usage  # Extract token usage

        # Append AI response to message history -MEMORY WIP ToDO
        #messages.append({"role": "assistant", "content": content})

        if show_token_usage:
            return {"response": content, "usage": usage}  # Return both content and usage
        else:
            return {"response": content}

    elif model_provider == "groq":
        client = Groq(api_key=GROQ_API_KEY) 

        # Append new user query to message history -MEMORY WIP ToDO
        #messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            messages=messages,
            model=model_name,
            #temperature=0.2 #DO NOT SET THE TEMPERATURE HERE!
        )       
        content = response.choices[0].message.content  
        usage = response.usage  # Extract token usage

        # Append AI response to message history -MEMORY WIP ToDO
        #messages.append({"role": "assistant", "content": content})        

        if show_token_usage:
            return {"response": content, "usage": usage}  # Return both content and usage
        else:
            return {"response": content}
    