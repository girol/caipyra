from unittest.mock import ANY


def test_get_hello(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"Hello": "Caipyra"}


def test_get_environ(client):
    response = client.get("/env")

    assert response.status_code == 200
    assert response.json() == {"env": ANY}
