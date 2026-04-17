from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os
from utils import get_auto_cart_extra, get_item_meta

app = FastAPI(title="SmartCart AI", description="Predictive Retail Assistant API")

# Ensure the public directory exists before mounting
if os.path.exists("public"):
    app.mount("/static", StaticFiles(directory="public"), name="static")

@app.get("/")
def serve_frontend():
    """Serves the accessible semantic HTML frontend demo."""
    file_path = os.path.join("public", "index.html")
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"message": "SmartCart AI is running. Visit /docs for API documentation."}

class UserData(BaseModel):
    user_id: str
    purchase_history: list[str]

@app.post("/recommend")
def recommend(data: UserData):
    history = [item.lower() for item in data.purchase_history]
    recommendations = []

    if "milk" in history:
        recommendations.append("bread")
    if "chips" in history:
        recommendations.append("soda")
    if "formula" in history:
        recommendations.append("medicine")

    # Format output with ABC/VED data
    formatted_recs = []
    for rec in set(recommendations):
        meta = get_item_meta(rec)
        formatted_recs.append(f"{rec} (Class {meta['class']} / {meta['type']})")

    return {
        "recommendations": formatted_recs,
        "reason": "Based on frequent co-purchase patterns with VED-class awareness"
    }

@app.post("/auto-cart")
def auto_cart(data: UserData):
    base = [item.lower() for item in data.purchase_history]
    extra = get_auto_cart_extra(base)
    
    # Strip out Desirables out of base to prevent automating impulse carts
    refined_cart = [item for item in set(base + extra) if get_item_meta(item)["type"] != "Desirable"]

    formatted_cart = []
    for item in refined_cart:
        meta = get_item_meta(item)
        formatted_cart.append(f"{item} (Class {meta['class']} / {meta['type']})")

    return {
        "cart": formatted_cart,
        "confidence": "high",
        "reason": "Auto-compiled omitting Class-C impulse items to preserve budget"
    }

@app.post("/optimize-inventory")
def optimize():
    # Admin mock demand simulation
    return {
        "restock": ["formula (Class A / Vital)", "medicine (Class A / Vital)", "milk (Class B / Essential)"],
        "overstock": ["chips (Class C / Desirable)", "soda (Class C / Desirable)"],
        "reason": "Prioritizing ABC strictly: Class A stockout prevention vs Class C capital lockup"
    }
