import json
from app.clients.llm_client import LlmClient
from app.schemas.llm_service import GeneratedCard
from app.services.prompt import PromptService


class LlmService:
    def __init__(self, llm_client: LlmClient):
        self.llm_client = llm_client
        self.prompt_service = PromptService()

    def _remove_json_prefix(self, response: str) -> str:
        return response.replace("```json", "").replace("```", "")

    def generate_card(self) -> GeneratedCard:
        prompt = self.prompt_service.get_create_card_prompt()
        response = self.llm_client.generate_text(prompt)
        response = self._remove_json_prefix(response)
        card_data = json.loads(response)
        return GeneratedCard(**card_data)
