from datetime import datetime, timedelta, timezone

from fastapi.security import OAuth2PasswordBearer
from jose import jwt

from app.config import Config
from app.controllers.user import UserController
from app.repositories.user import UserRepository
from app.schemas.session import LoginView
from app.schemas.user import UserCreate, UserView

config = Config()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class SessionController:
    def __init__(
        self, user_repository: UserRepository, user_controller: UserController
    ):
        self.user_repository = user_repository
        self.user_controller = user_controller

    def _create_access_token(self, data: dict, expires_delta: timedelta):
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + expires_delta
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(
            to_encode, config.SECRET_KEY, algorithm=config.ALGORITHM
        )
        return encoded_jwt

    def login(self, username: str, avatar_id: int, email: str):
        user = self.user_repository.get_by_email(email)

        if not user:
            user = self.user_controller.create(
                UserCreate(username=username, avatar_id=avatar_id, email=email)
            )

        access_token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = self._create_access_token(
            data={"sub": str(user.id)},
            expires_delta=access_token_expires,
        )

        return LoginView(
            user=UserView.model_validate(user, from_attributes=True),
            token=access_token,
        )
