from fastapi import APIRouter, Depends

from app.session.controller import SessionController
from app.session.deps import get_session_controller
from app.session.schemas import LoginPayload, LoginView

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
