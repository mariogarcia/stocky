from fastapi import FastAPI
from stocky.api import api_router
from stocky.common.config import setup_event_sourcing

setup_event_sourcing()

app = FastAPI()
app.include_router(api_router)