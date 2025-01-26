import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv(Path(__file__).parent.parent / ".env", override=True)


class Config(BaseModel):
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: str = os.getenv("DB_PORT", "5433")
    DB_NAME: str = os.getenv("DB_NAME", "mydatabase")
    DB_USER: str = os.getenv("DB_USER", "myuser")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "mypassword")

    SECRET_KEY: str = os.getenv("SECRET_KEY", "my-secret")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 10080)
    )
