from fastapi import FastAPI
from .api import trucks, drivers, goods, shipments, shippers

app = FastAPI(title="Track & Ship", version="0.1.0")


app.include_router(trucks.router, prefix="/api")
app.include_router(drivers.router, prefix="/api")
app.include_router(goods.router, prefix="/api")
app.include_router(shipments.router, prefix="/api")
app.include_router(shippers.router, prefix="/api")


@app.get("/")
def main():
    return {"message": "Welcome to Track & Ship API"}
