from app.models import Card, Spoiler
from app.repositories.card import CardRepository
from app.controllers.base import BaseController
from app.repositories.spoiler import SpoilerRepository
from app.schemas.card import CardCreate
from app.schemas.card import CardUpdate
from app.services.llm import LlmService


class CardController(BaseController[Card, CardRepository, CardCreate, CardUpdate]):
    def __init__(
        self,
        card_repository: CardRepository,
        spoiler_repository: SpoilerRepository,
        llm_service: LlmService,
    ):
        super().__init__(Card, card_repository)
        self.spoiler_repository = spoiler_repository
        self.llm_service = llm_service

    def create(self) -> Card:
        generated_card = self.llm_service.generate_card()

        card = super().create(CardCreate(**generated_card.model_dump()))
        for spoiler in generated_card.spoilers:
            self.spoiler_repository.add(
                Spoiler(card_id=card.id, content=spoiler.content)
            )

        return card
