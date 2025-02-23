from typing import List
from pydantic import BaseModel


class GeneratedSpoilerTranslation(BaseModel):
    language_id: int
    content: str


class GeneratedSpoiler(BaseModel):
    translations: List[GeneratedSpoilerTranslation]


class GeneratedCardTranslation(BaseModel):
    language_id: int
    title: str
    description: str


class GeneratedCard(BaseModel):
    translations: List[GeneratedCardTranslation]
    spoilers: List[GeneratedSpoiler]
