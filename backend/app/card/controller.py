import random
from app.database.models import Card, CardTranslation, Spoiler, SpoilerTranslation
from app.card.repository import CardRepository
from app.base.controller import BaseController
from app.spoiler.repository import SpoilerRepository
from app.card.schemas import CardCreate, CardUpdate
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
        # TODO: Create block to not generate more than 10 cards by day.

        previous_card_titles = self.repository.get_all_card_titles()
        generated_card = self.llm_service.generate_card(previous_card_titles)

        translations = [
            CardTranslation(
                language_id=t.language_id,
                title=t.title,
                description=t.description,
            )
            for t in generated_card.translations
        ]
        card = self.repository.add(
            Card(
                translations=translations,
            )
        )

        random.shuffle(generated_card.spoilers)

        for spoiler in generated_card.spoilers:
            spoiler_translations = [
                SpoilerTranslation(
                    language_id=t.language_id,
                    content=t.content,
                )
                for t in spoiler.translations
            ]
            self.spoiler_repository.add(
                Spoiler(
                    card_id=card.id,
                    translations=spoiler_translations,
                )
            )

        return card
