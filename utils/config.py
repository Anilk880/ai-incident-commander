import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(".env", override=True)

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env")

client = OpenAI(api_key=api_key)

MODEL = "gpt-4o-mini"
