import requests


def test_func_transaction(get_endpoint_url):
    response = requests.request("GET", get_endpoint_url)
    assert response.status_code == 200
    assert  response.json().get("status") == "success"