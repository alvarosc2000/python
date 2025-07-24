import sys
import os
import pytest
from fastapi.testclient import TestClient

# Para importar desde el nivel del main
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import app

client = TestClient(app)

# Estado compartido entre tests
state = {"created_id": None}

# Datos de ejemplo
test_game = {
    "name": "Catan",
    "publisher": "Klaus Teuber",
    "year": 1995,
    "rating": 4.5,
    "genre": "Strategy"
}

def test_create_game():
    response = client.post("/boardgames/create", json=test_game)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Catan"
    state["created_id"] = data["id"]

def test_get_game_by_id():
    response = client.get(f"/boardgames/{state['created_id']}")
    assert response.status_code == 200
    assert response.json()["name"] == "Catan"

def test_get_all_games():
    response = client.get("/boardgames")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_game():
    updated_game = test_game.copy()
    updated_game["rating"] = 4.8
    updated_game["name"] = "Catan Updated"
    response = client.put(f"/boardgames/update?id={state['created_id']}", json=updated_game)
    assert response.status_code == 200
    assert response.json()["rating"] == 4.8
    assert response.json()["name"] == "Catan Updated"

def test_delete_game():
    response = client.delete(f"/boardgames/{state['created_id']}")
    assert response.status_code == 200
    assert response.json()["message"] == "Juego eliminado"

def test_get_deleted_game():
    response = client.get(f"/boardgames/{state['created_id']}")
    assert response.status_code == 404
