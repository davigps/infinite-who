from app.clients.llm_client import LlmClient
from app.config import Config


def get_llm_client() -> LlmClient:
    return LlmClient(api_key=Config().GEMINI_API_KEY)
