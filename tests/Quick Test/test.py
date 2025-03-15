import os
from dotenv import load_dotenv

from docore_ai import intelligence_profiler # Sample DoCoreAI program to demonstrate

dotenv_loaded=load_dotenv()
print("Welcome to DoCoreAI - Intelligence Profiler")
print("DEBUG: dotenv loaded?", dotenv_loaded)
print("DEBUG: ENV VARIABLES:")
#print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))
print("MODEL_PROVIDER:", os.getenv("MODEL_PROVIDER"))# DEFAULT_MODEL='' - use 'openai','groq' etc in .env file
print("MODEL_NAME:", os.getenv("MODEL_NAME"))# MODEL='' - use   'gpt-3.5-turbo', 'gemma2-9b-it etc' in the .env file

def main():
    print(
        intelligence_profiler("What is one good way to start python coding for a experienced programmer","AI Developer",
                              os.getenv("MODEL_PROVIDER"),
                              os.getenv("MODEL_NAME")))

if __name__=="__main__":
    main()