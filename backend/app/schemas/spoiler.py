from datetime import datetime
from pydantic import BaseModel


class SpoilerBase(BaseModel):
    content: str
    card_id: int


class SpoilerCreate(SpoilerBase):
    pass


class SpoilerUpdate(BaseModel):
    content: str | None = None


class Spoiler(SpoilerBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
