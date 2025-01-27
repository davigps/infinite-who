from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.deps import get_session
from app.models import User
from app.repositories.user import UserRepository


def get_user_repository(session: Session = Depends(get_session)):
    return UserRepository(User, session)
