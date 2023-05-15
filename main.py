from fastapi import FastAPI
from api.trucks import router as trucks_router
from db_config.connect import engine, Base

api = FastAPI(title="Track & Ship", version="0.1.0")


api.include_router(trucks_router, prefix="/api")
