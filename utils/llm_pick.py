import sys

try:
    from langchain_openai import ChatOpenAI
except ModuleNotFoundError as exc:
    if exc.name != "langchain_openai":
        raise
    raise ModuleNotFoundError(
        "langchain_openai is not installed in the Python environment running this "
        f"script ({sys.executable}). Install it with: "
        f'"{sys.executable}" -m pip install langchain-openai'
    ) from exc
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

def pick_llm(Level: str) -> str:
    """
    Pick the appropriate LLM based on the level of complexity.

    Args:
        Level (str): The level of complexity ('simple', 'medium', 'complex').

    Returns:
        str: The name of the selected LLM.
    """
    if Level.lower() == "low":
        llm = ChatOpenAI(model_name="gpt-5.6-luna", temperature=0, model_kwargs={
        "reasoning_effort": "none"
        })
    elif Level.lower() == "medium":
        llm = ChatOpenAI(model_name="gpt-5.6-terra", temperature=0)
    elif Level.lower() == "complex":
        llm = ChatOpenAI(model_name="gpt-5.6-sol", temperature=0)
    else:
        raise ValueError("Invalid level. Choose from 'simple', 'medium', or 'complex'.")
    return llm