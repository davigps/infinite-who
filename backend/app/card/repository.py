from typing import List
from app.database.models import Card
from app.base.repository import BaseRepository


class CardRepository(BaseRepository[Card]):
    def get_all_card_titles(self) -> List[str]:
        # Eventually, we should add RAG to this
        return [card.title for card in self.session.query(Card).all()]
