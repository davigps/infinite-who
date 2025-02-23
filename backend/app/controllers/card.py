from app.models import Card
from app.repositories.card import CardRepository
from app.controllers.base import BaseController
from app.schemas.card import CardCreate
from app.schemas.card import CardUpdate
from app.services.llm import LlmService


class CardController(BaseController[Card, CardRepository, CardCreate, CardUpdate]):
    def __init__(self, card_repository: CardRepository, llm_service: LlmService):
        super().__init__(Card, card_repository)
        self.llm_service = llm_service

    def create(self) -> Card:
        generated_card = self.llm_service.generate_card()
        return super().create(generated_card)
