from fastapi import Depends
from app.llm.client import LlmClient
from app.config import Config
from app.llm.service import LlmService


def get_llm_client() -> LlmClient:
    return LlmClient(api_key=Config().GEMINI_API_KEY)


def get_llm_service(llm_client: LlmClient = Depends(get_llm_client)) -> LlmService:
    return LlmService(llm_client)
