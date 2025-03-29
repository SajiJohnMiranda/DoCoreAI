import os
from dotenv import load_dotenv

from docore_ai.model import intelligence_profiler,normal_prompt  # Test DoCoreAI program 

dotenv_loaded=load_dotenv()
print("Welcome to DoCoreAI - Intelligence Profiler")
print("DEBUG: dotenv loaded?", dotenv_loaded)
print("DEBUG: ENV VARIABLES:")
#print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))
print("MODEL_PROVIDER:", os.getenv("MODEL_PROVIDER"))# DEFAULT_MODEL='' - use 'openai','groq' etc in .env file
print("MODEL_NAME:", os.getenv("MODEL_NAME"))# MODEL='' - use   'gpt-3.5-turbo', 'gemma2-9b-it etc' in the .env file

# TESTERS can change it here
PROMPT ='What is one good way to start python coding for a experienced programmer'
ROLE='AI Developer'

def main():
    print('Normal Response:')
    print('---------------')
    print(
        normal_prompt(PROMPT,ROLE,
                              os.getenv("MODEL_PROVIDER"),
                              os.getenv("MODEL_NAME")))
    print('*---------------')
    print('---------------*')
    print('DoCoreAI Response:')
    print('-----------------')
    print(
        intelligence_profiler(PROMPT,ROLE,
                              os.getenv("MODEL_PROVIDER"),
                              os.getenv("MODEL_NAME")))
    print('*---------------')
    print('---------------*')
if __name__=="__main__":
    main()