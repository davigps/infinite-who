import random

from app.database.models import Card, Spoiler
from app.card.repository import CardRepository
from app.base.controller import BaseController
from app.spoiler.repository import SpoilerRepository
from app.card.schemas import CardCreate
from app.card.schemas import CardUpdate
from app.llm.service import LlmService


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
        previous_card_titles = self.repository.get_all_card_titles()
        generated_card = self.llm_service.generate_card(previous_card_titles)

        card = super().create(CardCreate(**generated_card.model_dump()))

        random.shuffle(generated_card.spoilers)

        for spoiler in generated_card.spoilers:
            self.spoiler_repository.add(
                Spoiler(card_id=card.id, content=spoiler.content)
            )

        return card
