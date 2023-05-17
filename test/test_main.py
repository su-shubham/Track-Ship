import pytest
from ..track_it.main import api as main
from httpx import AsyncClient


@pytest.mark.anyio
async def test_main():
    async with AsyncClient(app=main, base_url="http://test") as ac:
        response = await ac.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Welcome to Track & Ship API"}
