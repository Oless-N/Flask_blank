import requests


def test_health():

    url = "http://localhost:5050/health"

    response = requests.request("GET", url)
    assert response.status_code == 200
    assert response.json().get("status") == "success"
