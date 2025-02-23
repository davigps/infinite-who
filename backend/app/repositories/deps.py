from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.deps import get_session
from app.models import Spoiler, User
from app.models import Card
from app.repositories.spoiler import SpoilerRepository
from app.repositories.user import UserRepository
from app.repositories.card import CardRepository


def get_user_repository(session: Session = Depends(get_session)):
    return UserRepository(User, session)


def get_card_repository(session: Session = Depends(get_session)):
    return CardRepository(Card, session)


def get_spoiler_repository(session: Session = Depends(get_session)):
    return SpoilerRepository(Spoiler, session)
