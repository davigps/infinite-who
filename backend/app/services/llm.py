import json
from app.clients.llm_client import LlmClient
from app.schemas.card import CardCreate
from app.services.prompt import PromptService


class LlmService:
    def __init__(self, llm_client: LlmClient):
        self.llm_client = llm_client
        self.prompt_service = PromptService()

    def generate_card(self) -> CardCreate:
        prompt = self.prompt_service.get_create_card_prompt()
        response = self.llm_client.generate_text(prompt)
        print(response)
        card_data = json.loads(response)
        return CardCreate(**card_data)
