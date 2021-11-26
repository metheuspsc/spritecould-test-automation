import requests

BASE_URL = "https://petstore.swagger.io/v2/pet"


def post_pet(pet):
    return requests.post(BASE_URL, json=pet)


def get_pet_by_id(pet_id):
    return requests.get(BASE_URL + "/" + str(pet_id))


def update_pet(updated_pet):
    return requests.put(BASE_URL, json=updated_pet)


def update_pet_by_id(pet_id, name, status):
    return requests.post(BASE_URL + fr"/{pet_id}", data={"name": name, "status": status})


def delete_pet(pet_id):
    return requests.post(BASE_URL + fr"/{pet_id}", data={"api_key": "special_key"})