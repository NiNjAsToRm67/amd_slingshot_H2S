INVENTORY_DB = {
    "medicine": {"class": "A", "type": "Vital"},
    "formula": {"class": "A", "type": "Vital"},
    "milk": {"class": "B", "type": "Essential"},
    "bread": {"class": "B", "type": "Essential"},
    "eggs": {"class": "B", "type": "Essential"},
    "vegetables": {"class": "B", "type": "Essential"},
    "chips": {"class": "C", "type": "Desirable"},
    "soda": {"class": "C", "type": "Desirable"},
    "chocolate": {"class": "C", "type": "Desirable"}
}

def get_item_meta(item_name: str) -> dict:
    """Helper to fetch ABC/VED metadata for an item. Defaults to C/Desirable for unknowns."""
    return INVENTORY_DB.get(item_name.lower(), {"class": "C", "type": "Desirable"})

def get_auto_cart_extra(history: list[str]) -> list[str]:
    """Helper utility to determine extra items to suggest based on history."""
    extras = []
    # If they buy milk, predict bread, but verify class
    if "milk" in history and "bread" not in history:
        extras.append("bread")
    if "formula" in history and "medicine" not in history:
        extras.append("medicine")
        
    # We strip out Desirable items from automatic repurchasing routines
    final_extras = [item for item in extras if get_item_meta(item)["type"] != "Desirable"]
    return final_extras
