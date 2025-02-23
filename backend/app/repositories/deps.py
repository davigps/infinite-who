from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.deps import get_session
from app.models import User
from app.models import Card
from app.repositories.user import UserRepository
from app.repositories.card import CardRepository


def get_user_repository(session: Session = Depends(get_session)):
    return UserRepository(User, session)


def get_card_repository(session: Session = Depends(get_session)):
    return CardRepository(Card, session)
