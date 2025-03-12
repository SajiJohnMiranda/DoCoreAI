import os
from dotenv import load_dotenv

# Load .env file automatically when docoreai is imported
load_dotenv()

# Expose function 
from .model import intelligence_profiler  # Developer -> from docore_ai import intelligence_profiler



