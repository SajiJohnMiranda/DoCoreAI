# Pip installation setup for users
from setuptools import setup, find_packages

setup(
    name="coreai",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "pydantic",
        "python-dotenv",
        "openai",
        "langchain",
        "groq"
    ],
    entry_points={
        "console_scripts": [
            "coreai-run = coreai.api:run"
        ]
    },
)
