from datetime import datetime
from pydantic import BaseModel


class CardMapView(BaseModel):
    id: int
    title: str


class CardView(BaseModel):
    id: int
    title: str
    description: str
    created_at: datetime
    updated_at: datetime


class CardBase(BaseModel):
    title: str
    description: str


class CardCreate(CardBase):
    pass


class CardUpdate(CardBase):
    pass
