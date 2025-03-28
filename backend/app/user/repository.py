from typing import Optional

from app.database.models import User
from app.base.repository import BaseRepository


class UserRepository(BaseRepository[User]):
    def get_by_email(self, email: str) -> Optional[User]:
        return self.default_query.filter_by(email=email).first()

    def get_by_username(self, username: str) -> Optional[User]:
        return self.default_query.filter_by(username=username).first()
