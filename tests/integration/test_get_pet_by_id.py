import requests


def test_get_pet_by_id():
    response = requests.get(f"https://petstore.swagger.io/v2/pet/{1}")
    assert response.status_code == 200
