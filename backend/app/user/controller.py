from app.base.controller import BaseController
from app.database.models import User
from app.user.repository import UserRepository
from app.user.schemas import UserCreate, UserUpdate


class UserController(BaseController[User, UserRepository, UserCreate, UserUpdate]):
    pass
