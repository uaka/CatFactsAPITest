import requests

# Base URL of the Cat Facts API
BASE_URL = "https://catfact.ninja"


def test_get_random_fact():
    """
    Test Case 1: Verify that the API returns a random cat fact.

    Steps:
    1. Send a GET request to /fact endpoint.
    2. Verify the response status code is 200.
    3. Ensure the response contains a "fact" field and is a non-empty string.
    4. Ensure the response contains a "length" field that matches the length of the fact.
    """
    response = requests.get(f"{BASE_URL}/fact")

    # Validate HTTP status code
    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"

    data = response.json()

    # Validate the structure of the response
    assert "fact" in data, "Response does not contain 'fact' key"
    assert "length" in data, "Response does not contain 'length' key"

    # Validate that the fact is not empty
    assert isinstance(data["fact"], str) and len(data["fact"]) > 0, "Fact is empty or not a string"

    # Validate that length field is correct
    assert data["length"] == len(data["fact"]), "Fact length does not match 'length' field"


def test_get_multiple_facts():
    """
    Test Case 2: Verify that the API returns multiple cat facts.

    Steps:
    1. Send a GET request to /facts endpoint with a limit of 3.
    2. Verify the response status code is 200.
    3. Ensure the response contains a "data" field, which is a list.
    4. Ensure the list contains exactly 3 facts.
    5. Validate that each fact is a non-empty string.
    """
    response = requests.get(f"{BASE_URL}/facts?limit=3")

    # Validate HTTP status code
    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"

    data = response.json()

    # Validate response structure
    assert "data" in data, "Response does not contain 'data' key"
    assert isinstance(data["data"], list), "'data' field is not a list"
    assert len(data["data"]) == 3, f"Expected 3 facts, but got {len(data['data'])}"

    # Validate that each fact is a non-empty string
    for fact in data["data"]:
        assert isinstance(fact["fact"], str) and len(fact["fact"]) > 0, "One of the facts is empty or not a string"
