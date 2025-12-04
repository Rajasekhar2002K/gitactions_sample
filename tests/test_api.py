import requests
import time

BASE_URL = "http://localhost:5000"

# http://sample-service:5000/ping

def test_ping():
    time.sleep(1)
    res = requests.get(f"{BASE_URL}/ping")
    assert res.status_code == 200
    assert res.json()["message"] == "pong"

def test_user_1():
    res = requests.get(f"{BASE_URL}/user/1")
    assert res.status_code == 200
    assert res.json()["name"] == "Alice"

def test_user_not_found():
    res = requests.get(f"{BASE_URL}/user/999")
    assert res.status_code == 404