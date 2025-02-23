from fastapi import Depends

from app.controllers.session import SessionController
from app.controllers.user import UserController
from app.models import User
from app.repositories.deps import (
    get_card_repository,
    get_spoiler_repository,
    get_user_repository,
)
from app.repositories.spoiler import SpoilerRepository
from app.repositories.user import UserRepository
from app.repositories.card import CardRepository
from app.services.llm import LlmService
from app.services.deps import get_llm_service
from app.controllers.card import CardController


def get_user_controller(
    repository: UserRepository = Depends(get_user_repository),
):
    return UserController(User, repository)


def get_session_controller(
    user_repository: UserRepository = Depends(get_user_repository),
    user_controller: UserController = Depends(get_user_controller),
):
    return SessionController(user_repository, user_controller)


def get_card_controller(
    card_repository: CardRepository = Depends(get_card_repository),
    spoiler_repository: SpoilerRepository = Depends(get_spoiler_repository),
    llm_service: LlmService = Depends(get_llm_service),
):
    return CardController(card_repository, spoiler_repository, llm_service)
