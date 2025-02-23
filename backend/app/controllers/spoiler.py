from app.models import Spoiler
from app.repositories.spoiler import SpoilerRepository
from app.controllers.base import BaseController
from app.schemas.spoiler import SpoilerCreate
from app.schemas.spoiler import SpoilerUpdate


class SpoilerController(
    BaseController[Spoiler, SpoilerRepository, SpoilerCreate, SpoilerUpdate]
):
    pass
