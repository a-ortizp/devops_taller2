import pytest

from application import application


@pytest.fixture
def client():
    application.config["TESTING"] = True
    with application.test_client() as client:
        yield client


def test_index_retorna_todos_los_heroes(client):
    response = client.get("/")

    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 6
    assert data["0"]["name"] == "A-Bomb"


def test_heroe_retorna_el_heroe_por_id(client):
    response = client.get("/1")

    assert response.status_code == 200
    data = response.get_json()
    assert data["name"] == "Abe Sapien"
    assert data["publisher"] == "Dark Horse Comics"
    assert data["weight"] == "65"
