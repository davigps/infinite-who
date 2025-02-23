from app.card.repository import CardRepository
from sqlalchemy.orm import Session
from fastapi import Depends

from app.database.deps import get_session
from app.database.models import Card
from app.llm.deps import get_llm_service
from app.spoiler.deps import get_spoiler_repository
from app.spoiler.repository import SpoilerRepository
from app.llm.service import LlmService
from app.card.controller import CardController


def get_card_repository(session: Session = Depends(get_session)):
    return CardRepository(Card, session)


def get_card_controller(
    card_repository: CardRepository = Depends(get_card_repository),
    spoiler_repository: SpoilerRepository = Depends(get_spoiler_repository),
    llm_service: LlmService = Depends(get_llm_service),
):
    return CardController(card_repository, spoiler_repository, llm_service)
