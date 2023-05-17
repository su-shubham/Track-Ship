from fastapi import FastAPI
from .api import trucks,drivers
api = FastAPI(title="Track & Ship", version="0.1.0")


api.include_router(trucks.router, prefix="/api")
api.include_router(drivers.router, prefix="/api")


@api.get("/")
def main():
    return {"message": "Welcome to Track & Ship API"}