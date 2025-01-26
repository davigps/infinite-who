from pydantic import BaseModel, Field

from app.schemas.user import UserView


class LoginPayload(BaseModel):
    email: str = Field(
        pattern=r"[A-z0-9_.\-]+@[A-z0-9]+\.[A-z]+(\.[A-z]+)*",
        json_schema_extra={
            "title": "Email",
            "description": "Email of the user",
            "examples": ["john.doe@gmail.com"],
        },
    )
    username: str = Field(
        min_length=3,
        max_length=20,
        description="Username of the user",
        examples=["john_doe"],
    )
    avatar_id: int = Field(
        description="Avatar ID of the user",
        examples=[1],
    )


class LoginView(BaseModel):
    token: str
    user: UserView
