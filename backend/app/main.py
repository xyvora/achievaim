from typing import Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

from app.api.deps import logger
from app.api.v1.api import api_router
from app.db import init_db

app = FastAPI()
app.include_router(api_router)
templates = Jinja2Templates(directory="app/templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup() -> None:  # pragma: no cover
    logger.info("Initializing the database")
    await init_db()


@app.get("/", include_in_schema=False)
def index(request: Request) -> Any:
    return templates.TemplateResponse("index.html", {"request": request})
