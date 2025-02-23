from fastapi import HTTPException


class UserNotFoundException(HTTPException):
    def __init__(self, email: str):
        super().__init__(
            status_code=404,
            detail=f"User with email {email} not found",
        )


class UserNotAllowed(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=403,
            detail="Operation forbidden for current user",
        )
