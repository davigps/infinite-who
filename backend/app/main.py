from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import time

from app.routes.users import users_router
from app.routes.sessions import sessions_router
from app.routes.cards import cards_router

app = FastAPI(title="Infinite Who", version="0.0.1")
start_time = time.time()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def get_health():
    return {"status": "ok"}


app.include_router(users_router)
app.include_router(sessions_router)
app.include_router(cards_router)
