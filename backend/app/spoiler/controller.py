from app.database.models import Spoiler
from app.spoiler.repository import SpoilerRepository
from app.base.controller import BaseController
from app.spoiler.schemas import SpoilerCreate
from app.spoiler.schemas import SpoilerUpdate


class SpoilerController(
    BaseController[Spoiler, SpoilerRepository, SpoilerCreate, SpoilerUpdate]
):
    pass
