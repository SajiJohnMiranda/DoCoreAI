# Pip installation setup for users
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="docoreai",
    version="0.1.0",
    author="Saji John",
    author_email="sajijohnmiranda@gmail.com",
    description="DoCoreAI is an intelligence profiler that optimizes prompts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SajiJohnMiranda/DoCoreAI",  # Update with your repo URL    
    packages=find_packages(),
    install_requires=[
        "uvicorn",
        "pydantic",
        "python-dotenv",
        "openai",
        "langchain",
        "groq"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",    
)
