from fastapi import status
from httpx import AsyncClient

from tortoise.contrib import test

from main import app


BASE_URL = "http://127.0.0.1:8000/api/v1"


class TestMain(test.TestCase):
    async def test_main(self):
        async with AsyncClient(app=app, base_url=BASE_URL) as ac:
                response = await ac.get("/")
        assert response.status_code == status.HTTP_200_OK
        
