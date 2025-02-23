from typing import List
from pydantic import BaseModel


class GeneratedSpoiler(BaseModel):
    content: str


class GeneratedCard(BaseModel):
    title: str
    description: str
    spoilers: List[GeneratedSpoiler]
