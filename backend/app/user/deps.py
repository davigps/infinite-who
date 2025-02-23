from app.database.models import User
from app.user.repository import UserRepository
from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.deps import get_session
from app.user.controller import UserController


def get_user_repository(session: Session = Depends(get_session)):
    return UserRepository(User, session)


def get_user_controller(
    repository: UserRepository = Depends(get_user_repository),
):
    return UserController(User, repository)
