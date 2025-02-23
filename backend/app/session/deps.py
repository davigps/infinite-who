from app.session.controller import SessionController
from app.user.deps import get_user_controller, get_user_repository
from app.user.controller import UserController
from fastapi import Depends

from app.user.repository import UserRepository


def get_session_controller(
    user_repository: UserRepository = Depends(get_user_repository),
    user_controller: UserController = Depends(get_user_controller),
) -> SessionController:
    return SessionController(
        user_repository=user_repository,
        user_controller=user_controller,
    )
