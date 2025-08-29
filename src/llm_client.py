import os
from dotenv import load_dotenv
load_dotenv()
import openai

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if OPENAI_API_KEY:
    openai.api_key = OPENAI_API_KEY

DEFAULT_MODEL = "gpt-3.5-turbo"

def ask_llm(system: str, user_prompt: str, model: str = DEFAULT_MODEL) -> str:
    """
    Returns LLM output string.
    Raises RuntimeError if API key missing.
    """
    if not OPENAI_API_KEY:
        raise RuntimeError("OPENAI_API_KEY is not set. Create .env with your key.")
    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": user_prompt}
    ]
    resp = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=400,
        temperature=0.2
    )
    return resp.choices[0].message.content.strip()