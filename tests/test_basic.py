from fastapi.testclient import TestClient
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import app


client = TestClient(app)

def test_hello_world():
    response = client.get("/hello_world")
    assert response.status_code == 200
    assert response.json() == "Hello, world!"
