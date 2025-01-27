from fastapi import Depends

from app.controllers.session import SessionController
from app.controllers.user import UserController
from app.models import User
from app.repositories.deps import get_user_repository
from app.repositories.user import UserRepository


def get_user_controller(
    repository: UserRepository = Depends(get_user_repository),
):
    return UserController(User, repository)


def get_session_controller(
    user_repository: UserRepository = Depends(get_user_repository),
    user_controller: UserController = Depends(get_user_controller),
):
    return SessionController(user_repository, user_controller)
