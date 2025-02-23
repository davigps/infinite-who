from datetime import datetime
from typing import List
from pydantic import BaseModel


class CardTranslationBase(BaseModel):
    language_id: int
    title: str
    description: str


class CardTranslationCreate(CardTranslationBase):
    pass


class CardTranslationUpdate(BaseModel):
    title: str | None = None
    description: str | None = None


class CardTranslation(CardTranslationBase):
    id: int
    card_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class CardMapView(BaseModel):
    id: int
    title: str  # This will be in the default language


class CardView(BaseModel):
    id: int
    translations: List[CardTranslation]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class CardCreate(BaseModel):
    translations: List[CardTranslationCreate]


class CardUpdate(BaseModel):
    translations: List[CardTranslationUpdate] | None = None
