from datetime import datetime, timezone
from pymongo import MongoClient

URI = "mongodb://labuser:labpassword@localhost:27017/?authSource=admin"


def main():
    client = MongoClient(URI)
    db = client["parcelflow"]
    result = db.inventory.update_one(
        {"sku": "SKU-0001", "available": {"$gte": 1}},
        {"$inc": {"available": -1}},
    )
    if result.modified_count != 1:
        raise RuntimeError("Inventory update did not succeed")
    order = {
        "orderId": f"LAB-{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S%f')}",
        "customerId": "C-0001",
        "status": "created",
        "createdAt": datetime.now(timezone.utc),
        "items": [{"sku": "SKU-0001", "quantity": 1, "unitPrice": 19.99}],
    }
    inserted = db.orders.insert_one(order)
    print("Created order:", inserted.inserted_id)


if __name__ == "__main__":
    main()
