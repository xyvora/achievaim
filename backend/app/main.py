from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.deps import logger
from app.api.v1.api import api_router
from app.db import init_db

app = FastAPI()
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup() -> None:
    logger.info("Initializing the database")
    await init_db()
