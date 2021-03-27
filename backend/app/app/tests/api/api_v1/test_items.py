from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.drug import create_random_drug


def test_create_drug(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    data = {"title": "Foo", "description": "Fighters"}
    response = client.post(
        f"{settings.API_V1_STR}/drugs/", headers=superuser_token_headers, json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == data["title"]
    assert content["description"] == data["description"]
    assert "id" in content
    assert "owner_id" in content


def test_read_drug(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    drug = create_random_drug(db)
    response = client.get(
        f"{settings.API_V1_STR}/drugs/{drug.id}", headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == drug.title
    assert content["description"] == drug.description
    assert content["id"] == drug.id
    assert content["owner_id"] == drug.owner_id
