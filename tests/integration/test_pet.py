import json

import pytest
import requests

BASE_URL = "https://petstore.swagger.io/v2/pet"
TEST_PET = {
    "id": 9999,
    "category": {"id": 9999, "name": "string"},
    "name": "Zelda",
    "photoUrls": ["string"],
    "tags": [{"id": 9999, "name": "string"}],
    "status": "available"
}


def test_post_pet():
    response = requests.post(BASE_URL, json=TEST_PET)
    assert response.status_code == 200


def test_get_pet_by_id():
    response = requests.get(BASE_URL + "/" + str(TEST_PET["id"]))
    assert response.status_code == 200
    assert response.json() == TEST_PET
