from datetime import datetime
from pydantic import BaseModel


class LanguageBase(BaseModel):
    code: str
    name: str


class LanguageCreate(LanguageBase):
    pass


class LanguageUpdate(LanguageBase):
    code: str | None = None
    name: str | None = None


class Language(LanguageBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
