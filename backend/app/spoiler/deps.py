from app.database.models import Spoiler
from app.spoiler.controller import SpoilerController
from app.spoiler.repository import SpoilerRepository
from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.deps import get_session


def get_spoiler_repository(session: Session = Depends(get_session)):
    return SpoilerRepository(Spoiler, session)


def get_spoiler_controller(
    repository: SpoilerRepository = Depends(get_spoiler_repository),
):
    return SpoilerController(Spoiler, repository)
