import os
from dotenv import load_dotenv

from docore_ai import intelligence_profiler # Sample DoCoreAI program to demonstrate

dotenv_loaded=load_dotenv()
print("Welcome to DoCoreAI - Intelligence Profiler")
print("DEBUG: dotenv loaded?", dotenv_loaded)
print("DEBUG: ENV VARIABLES:")
#print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))
print("DEFAULT_MODEL:", os.getenv("DEFAULT_MODEL"))# DEFAULT_MODEL='' - use 'openai','groq' etc in .env file
print("MODEL:", os.getenv("MODEL"))# MODEL='' - use   'gpt-3.5-turbo', 'gemma2-9b-it etc' in the .env file

def main():
    print(
        intelligence_profiler("What is one good way to start python coding for a experienced programmer","AI Developer",
                              os.getenv("DEFAULT_MODEL"),
                              os.getenv("MODEL")))

if __name__=="__main__":
    main()
