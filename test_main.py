from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_recommend():
    response = client.post("/recommend", json={
        "user_id": "U1",
        "purchase_history": ["milk"]
    })
    assert response.status_code == 200
    assert any("bread" in item for item in response.json()["recommendations"])

def test_auto_cart():
    response = client.post("/auto-cart", json={
        "user_id": "U2",
        "purchase_history": ["milk", "eggs"]
    })
    assert response.status_code == 200
    assert any("bread" in item for item in response.json()["cart"])
    assert response.json()["confidence"] == "high"

def test_auto_cart_strips_desirable():
    # Chips is desirable, so it should not be in the auto-cart
    response = client.post("/auto-cart", json={
        "user_id": "U3",
        "purchase_history": ["chips"]
    })
    assert response.status_code == 200
    assert len(response.json()["cart"]) == 0

def test_optimize_inventory():
    response = client.post("/optimize-inventory")
    assert response.status_code == 200
    assert "restock" in response.json()
    assert any("formula" in item for item in response.json()["restock"])
