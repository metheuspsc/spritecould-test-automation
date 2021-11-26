from conftest import post_pet, get_pet_by_id, update_pet, update_pet_by_id, delete_pet

TEST_PET = {
    "id": 9999,
    "category": {"id": 9999, "name": "string"},
    "name": "Zelda",
    "photoUrls": ["string"],
    "tags": [{"id": 9999, "name": "string"}],
    "status": "available"
}


def test_post_pet():
    """Tests adding a pet to the store"""
    response = post_pet(TEST_PET)
    assert response.status_code == 200


def test_get_pet_by_id():
    """Tests getting pet by id"""
    post_pet(TEST_PET)
    response = get_pet_by_id(TEST_PET["id"])
    assert response.status_code == 200
    assert response.json() == TEST_PET


def test_update_pet():
    """Tests updating a pet"""
    updated_pet = TEST_PET
    updated_pet["name"] = "Link"
    response = update_pet(updated_pet)
    assert response.status_code == 200
    pet = get_pet_by_id(TEST_PET["id"])
    assert updated_pet == pet.json()


def test_update_pet_by_id():
    """Tests updating a pet by id"""
    response = update_pet_by_id(TEST_PET["id"], "Ganon", "unavailable")
    assert response.status_code == 200
    pet = get_pet_by_id(TEST_PET["id"])
    assert pet.json()['name'] == "Ganon"


def test_delete_pet():
    response = delete_pet(TEST_PET["id"])
    assert response.status_code == 200
    check_deletion = get_pet_by_id(TEST_PET["id"])
    assert check_deletion.status_code == 404
