from fastapi.testclient import TestClient

from src.app.main import app

client = TestClient(app)


def test_get_user(client: TestClient) -> None:
    response = client.get(
        "/api/v1/user/me"
    )
    assert response.status_code == 201