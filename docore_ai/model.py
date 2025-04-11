import os
#import sys
import openai
import tiktoken
from typing import Optional
from groq import Groq
from research.Telm.jsonbin import update_jsonbin, is_telemetry_enabled
from dotenv import load_dotenv
import threading

if is_telemetry_enabled():
    try:
        thread = threading.Thread(target=update_jsonbin, args=("Upgrade",))
        thread.daemon = True  # Allows the program to exit even if telemetry is still running
        thread.start()
    except Exception as e:
        print(f"Error starting telemetry thread: {e}")    

if not os.path.exists(".env"):
    raise FileNotFoundError("⚠️ Missing .env file! Please create one with API keys. Refer to the README https://github.com/SajiJohnMiranda/DoCoreAI/.")

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_PROVIDER = os.getenv("MODEL_PROVIDER")  #'openai' , 'groq' etc
MODEL_NAME = os.getenv("MODEL_NAME")  # gpt-3.5-turbo, gemma2-9b-it 

def intelligence_profiler(user_content: str, role: str, model_provider: str = MODEL_PROVIDER, model_name: str = MODEL_NAME,
                          show_token_usage: Optional[bool] = False, estimated_cost: Optional[bool] = True) -> dict:
    #### LIVE -- LIVE---LIVE -- LIVE
    print(f"Profiler received prompt: {user_content}")
    print(f"Profiler received  Role: {role}")
    #print(f"intelligence_profiler model_provider : {model_provider}")
    print(f"Profiler Model: {model_name}")


    system_message = f"""
        You are an expert AI assistant. First, analyze the user query and determine optimal intelligence parameters:
        - Reasoning (0.1-1.0): Logical depth
        - Creativity (0.1-1.0): Imagination level
        - Precision (0.1-1.0): Specificity required
        - Openness (0.1-1.0): Imagination level, Creativity, Abstractness.
        - Rigor (0.1-1.0): Logical analysis, Precision, Exactness.        

        Based on these values, **derive the Temperature dynamically** as follows:
        - **calculate Temperature using the formula:** → **Temperature = clamp( (Openness+Creativity)/2 × 0.7 - (Rigor+Reasoning)/2 × 0.6 + 0.5, 0.1, 1.0)
        - If **Precision is high (≥0.8) and Reasoning is low (≤0.3)** → **Temperature = 0.2 to 0.3** 
        - If **Precision is high (≥0.8) and Creativity is low (≤0.2)** → **Temperature = 0.1 to 0.3**
        
        You MUST generate responses using the derived temperature value dynamically, ensuring coherent and informative response with the intelligence profile.
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
    try:
        if model_provider == "openai":
            openai.api_key = OPENAI_API_KEY
            print("🔑 Using OpenAI API...")
            print(f"OPENAI_API_KEY loaded: {len(OPENAI_API_KEY) if OPENAI_API_KEY else '❌ Not Found'}")


            response = openai.Client().chat.completions.create(
                model=model_name,
                messages=messages,
                #temperature=0.7 # Default - TEMPERATURE SETTING NOT REQUIRED!
            )
            print("✅ OpenAI API call successful")
            content = response.choices[0].message.content
            usage = response.usage  # Extract token usage


            result = {"response": content}

            if show_token_usage:
                result["usage"] = usage
            if estimated_cost:
                result["token_estimation"] = token_profiler(user_content, model_name)
            return result            

        elif model_provider == "groq":
            client = Groq(api_key=GROQ_API_KEY) 
            print("🔑 Using Groq API...")
            print(f"GROQ_API_KEY loaded: {len(GROQ_API_KEY) if GROQ_API_KEY else '❌ Not Found'}")


            # Append new user query to message history -MEMORY WIP ToDO
            #messages.append({"role": "user", "content": user_input})

            response = client.chat.completions.create(
                messages=messages,
                model=model_name,
                #temperature=0 #TEMPERATURE SETTING NOT REQUIRED - for Intelligence Profiler Prompt
            )       
            print("✅ Groq API call successful")
            content = response.choices[0].message.content  
            usage = response.usage  # Extract token usage

            # Append AI response to message history -MEMORY WIP ToDO
            #messages.append({"role": "assistant", "content": content})        

            '''if show_token_usage:
                return {"response": content, "usage": usage}  # Return both content and usage
            if estimated_cost:
                return {"response": content, "token_estimation": token_profiler(user_content, model_name)} 
            else:
                return {"response": content}'''
            result = {"response": content}

            if show_token_usage:
                result["usage"] = usage
            if estimated_cost:
                result["token_estimation"] = token_profiler(user_content, model_name)
            return result            
    except Exception as e:
        print("❌ Exception during API call - intelligence_profiler:", e)
        return {"response": None, "error": str(e)}
#Added only for tetsting
def normal_prompt(user_content: str, role: str, model_provider: str = MODEL_PROVIDER, model_name: str = MODEL_NAME, 
                  show_token_usage: Optional[bool] = True) -> dict:
    """  Sends a normal prompt to the selected LLM (OpenAI or Groq) without intelligence parameters.
    """
    system_message = f"""
    You are an AI assistant. Your goal is to respond to user queries based on your expertise.

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
            temperature=0.8 #Check Groq default temp
        )       
        content = response.choices[0].message.content  
        usage = response.usage  # Extract token usage

        if show_token_usage:
            return {"response": content, "usage": usage}  # Return both content and usage
        else:
            return {"response": content}


def token_profiler(prompt: str, model_name) -> dict:
    # --- 1. Estimate token count ---
    try:
        encoding = tiktoken.encoding_for_model(model_name)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")  # fallback

    token_count = len(encoding.encode(prompt))

    # --- 2. Estimate cost (simplified) ---
    # Source: https://openai.com/pricing
    price_per_1k = {
        "gpt-3.5-turbo": 0.0015,
        "gpt-4": 0.03,
        "gpt-4-turbo": 0.01,
        "gemma-2b": 0.0005,
        "gemma-9b": 0.001,
    }
    
    cost_per_token = price_per_1k.get(model_name, 0.0015) / 1000
    estimated_cost = round(token_count * cost_per_token, 6)

    # --- 3. Heuristic Bloat Score ---
    word_count = len(prompt.split())
    avg_tokens_per_word = token_count / word_count if word_count else 0

    bloat_score_raw = avg_tokens_per_word / 1.2  # 1.2 is healthy average
    bloat_score = round(bloat_score_raw, 2)
    bloat_flag = bloat_score_raw > 1.1  # Only flag if noticeably bloated

    # --- 4. Estimate potential savings if optimized ---
    savings_ratio = 0.3 if bloat_flag else 0.0
    estimated_savings = round(estimated_cost * savings_ratio, 6)
    savings_percent = f"{int(savings_ratio * 100)}%"
    
    return {
        "token_count": token_count,
        "estimated_cost": f"${estimated_cost:.6f}",
        "bloat_score": round(bloat_score, 2),
        "bloat_flag": bloat_flag,
        "estimated_savings_if_optimized": f"${estimated_savings:.6f}",
        "estimated_savings%_if_optimized": savings_percent
    }

'''
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

'''
'''
        - Reasoning (0.1-1.0): Logical depth
        - Creativity (0.1-1.0): Imagination level
        - Precision (0.1-1.0): Specificity required
        - Openness (0.1-1.0): Imagination level, Creativity, Abstractness.
        - Rigor (0.1-1.0): Logical analysis, Precision, Exactness.        

        Based on these values, **calculate the Temperature (T) using the formula:**
            Temperature = clamp( (Openness+Creativity)/2 × 0.7 - (Rigor+Reasoning)/2 × 0.6 + 0.5, 0.1, 1.0)
        You MUST generate responses using the derived temperature value dynamically, ensuring coherence with the intelligence profile.


'''
#            T = clamp(0.2 + 0.75 * Creativity - 0.4 * Precision + 0.2 * (1 - Reasoning), 0.1, 1.0)

#            T = 1 - [0.5 × Precision + 0.3 × Reasoning - 0.4 × Creativity + |Precision - Creativity| × (1 - Reasoning)²]  


'''
https://pypi.org/project/docoreai/  -- docoreai 0.2.4

    system_message = f"""
        You are an expert AI assistant. First, analyze the user query and determine optimal intelligence parameters:
        - Reasoning (0.1-1.0): Logical depth
        - Creativity (0.1-1.0): Imagination level
        - Precision (0.1-1.0): Specificity required
        - Openness (0.1-1.0): Imagination level, Creativity, Abstractness.
        - Rigor (0.1-1.0): Logical analysis, Precision, Exactness.        

        Based on these values, **derive the Temperature dynamically** as follows:
        - **calculate Temperature using the formula:** → **Temperature = clamp( (Openness+Creativity)/2 × 0.7 - (Rigor+Reasoning)/2 × 0.6 + 0.5, 0.1, 1.0)
        - If **Precision is high (≥0.8) and Reasoning is low (≤0.3)** → **Temperature = 0.2 to 0.3** 
        - If **Precision is high (≥0.8) and Creativity is low (≤0.2)** → **Temperature = 0.1 to 0.3**
        
        You MUST generate responses using the derived temperature value dynamically, ensuring coherent and informative response with the intelligence profile.
        Then, generate a response based on these parameters. 

        Return **ONLY** the following JSON format:  
        {{
            "optimized_response": "<AI-generated response>",
            "intelligence_profile": {{ "reasoning": <value>, "creativity": <value>, "precision": <value>, "temperature": <value> # Internally used}}
        }}
    """
    #Version 0.3.0 :10-04-2025
        system_message = f"""
        You are an expert AI assistant. First, analyze the user query and determine optimal intelligence parameters:
        - Reasoning (0.1-1.0): Logical depth
        - Creativity (0.1-1.0): Imagination level
        - Precision (0.1-1.0): Specificity required
        - Openness (0.1-1.0): Imagination level, Creativity, Abstractness.
        - Rigor (0.1-1.0): Logical analysis, Precision, Exactness.        

        Based on these values, **derive the Temperature dynamically** as follows:
        - **calculate Temperature using the formula:** → **Temperature = clamp( (Openness+Creativity)/2 × 0.69 - (Rigor+Reasoning+Precision)/2 × 0.7 + 0.5, 0.1, 1.0)
        - if (Precision+Rigor)/2 ≥0.7:  → Temperature = (0.0-0.3)
        - if (Reasoning+Rigor+Precision+Creativity+Openness)/5 ≥0.7:  → Temperature = (0.7-1.1) 
        
        You MUST generate responses using the derived temperature value dynamically, ensuring coherent and informative response with the intelligence profile.
        Then, generate a response based on these parameters. 

        Return **ONLY** the following JSON format:  
        {{
            "optimized_response": "<AI-generated response>",
            {{ "temperature": <value>}}
        }}
    """

    #Version 0.3.1 :11-04-2025 - Best
    system_message = f"""
        You are a system prompt profiler. Analyze the user input and estimate what temperature setting would best match the tone, ambiguity, and specificity of the request.
        Return the estimated temperature value only, between 0.1 and 1.0, based on the following:
        - Low temperature (~0.1–0.3): Precise, factual, deterministic answers.
        - Medium temperature (~0.4–0.6): Balanced creativity and reasoning.
        - High temperature (~0.7–1.0): Creative, open-ended, speculative, or abstract.

        You MUST generate responses using the estimated temperature.
        The response must be coherent and informative

        Return **ONLY** the following JSON format:  
        {{
            "optimized_response": "<AI-generated response>",
            {{ "temperature": <value>}}
        }}
    """
    user_message = f"""
    User Request: "{user_content}"
    Role: "{role}"
    """


'''