from fastapi import APIRouter, Depends

from app.controllers.deps import get_card_controller
from app.controllers.card import CardController
from app.schemas.card import CardView
from app.services import auth

cards_router = APIRouter(
    dependencies=[Depends(auth.get_logged_user)],
)


@cards_router.post(
    "/cards",
    tags=["cards"],
    response_model=CardView,
    description="Create a new card",
)
def create_card(
    controller: CardController = Depends(get_card_controller),
):
    return controller.create()
