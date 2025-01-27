from fastapi import APIRouter, Depends

from app.controllers.deps import get_session_controller
from app.controllers.session import SessionController
from app.schemas.session import LoginPayload, LoginView

sessions_router = APIRouter()


@sessions_router.post(
    "/sessions",
    tags=["sessions"],
    response_model=LoginView,
    description="Return JWT Token and User information",
)
def make_login(
    body: LoginPayload,
    controller: SessionController = Depends(get_session_controller),
):
    return controller.login(body.username, body.avatar_id, body.email)
