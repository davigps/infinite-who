from fastapi import APIRouter, Depends

from app.card.controller import CardController
from app.card.deps import get_card_controller
from app.card.schemas import CardView
from app.session.middlewares import get_logged_user

cards_router = APIRouter(
    dependencies=[Depends(get_logged_user)],
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
