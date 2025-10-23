from molotov import scenario
import json

@scenario(weight=1)
async def test_hello(session):
    async with session.get("http://localhost:8000/api/hello") as resp:
        assert resp.status == 200
        data = await resp.json()
        assert "message" in data
