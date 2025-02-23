from app.controllers.base import BaseController
from app.models import User
from app.repositories.user import UserRepository
from app.schemas.user import UserCreate, UserUpdate


class UserController(BaseController[User, UserRepository, UserCreate, UserUpdate]):
    pass
