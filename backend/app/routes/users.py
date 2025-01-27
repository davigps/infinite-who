from fastapi import APIRouter, Depends

from app.controllers.deps import get_user_controller
from app.controllers.user import UserController
from app.schemas.user import (
    UserCreate,
    UserUpdate,
    UserView,
)
from app.services import auth

users_router = APIRouter()


@users_router.post(
    "/users",
    tags=["users"],
    response_model=UserView,
    description="Create a new user",
)
def create_user(
    body: UserCreate, controller: UserController = Depends(get_user_controller)
):
    return controller.create(body)


@users_router.get("/users/me", tags=["users"], response_model=UserView)
def get_user(
    controller: UserController = Depends(get_user_controller),
    user: UserView = Depends(auth.get_logged_user),
):
    return controller.get_by_id(user.id)


@users_router.patch("/users/me", tags=["users"], response_model=UserView)
def update_user(
    body: UserUpdate,
    controller: UserController = Depends(get_user_controller),
    user: UserView = Depends(auth.get_logged_user),
):
    return controller.update(user.id, body)


@users_router.delete("/users/me", tags=["users"])
def delete_user(
    controller: UserController = Depends(get_user_controller),
    user: UserView = Depends(auth.get_logged_user),
):
    return controller.delete(user.id)
