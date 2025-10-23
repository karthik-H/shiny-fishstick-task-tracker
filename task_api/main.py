from fastapi import FastAPI
from .api import tasks

app = FastAPI()

app.include_router(tasks.router)
