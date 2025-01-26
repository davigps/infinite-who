from app.controllers.base import BaseController
from app.models import User
from app.repositories.user import UserRepository
from app.schemas.user import UserCreate, UserUpdate


class UserController(BaseController[User, UserRepository, UserCreate, UserUpdate]):
    def update(self, id: int, update: UserUpdate):
        return super().update(id, update)
