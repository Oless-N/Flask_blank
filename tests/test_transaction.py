import requests


def test_func_transaction(get_endpoint_url):
    h = {'client_id': "10203046789"}
    response = requests.request("GET", get_endpoint_url, headers=h)
    assert response.status_code == 200
    assert response.json().get("result") == "OK"
