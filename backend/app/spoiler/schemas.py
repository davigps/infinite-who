from datetime import datetime
from typing import List
from pydantic import BaseModel


class SpoilerTranslationBase(BaseModel):
    language_id: int
    content: str


class SpoilerTranslationCreate(SpoilerTranslationBase):
    pass


class SpoilerTranslationUpdate(BaseModel):
    content: str | None = None


class SpoilerTranslation(SpoilerTranslationBase):
    id: int
    spoiler_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class SpoilerBase(BaseModel):
    card_id: int


class SpoilerCreate(SpoilerBase):
    translations: List[SpoilerTranslationCreate]


class SpoilerUpdate(BaseModel):
    translations: List[SpoilerTranslationUpdate] | None = None


class Spoiler(SpoilerBase):
    id: int
    translations: List[SpoilerTranslation]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
