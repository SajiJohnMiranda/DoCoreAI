# Pip installation setup for users
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="docoreai",
    version="0.1.2",
    author="Saji John",
    author_email="sajijohnmiranda@gmail.com",
    description="DoCoreAI is an intelligence profiler that optimizes prompts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SajiJohnMiranda/DoCoreAI",  # Update with your repo URL    
    project_urls={
        "Documentation": "https://your-docs-url.com",
        "Blog Post": "https://mobilights.medium.com/intelligent-prompt-optimization-bac89b64fa84",
        "Source Code": "https://github.com/SajiJohnMiranda/DoCoreAI",
    },        
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
print("\n✅ Installation complete! Please create a `.env` file in your root folder. Refer to the README for details.\n")
