from fastapi import Depends
from app.clients.deps import get_llm_client
from app.clients.llm_client import LlmClient
from app.services.llm import LlmService


def get_llm_service(llm_client: LlmClient = Depends(get_llm_client)) -> LlmService:
    return LlmService(llm_client)
