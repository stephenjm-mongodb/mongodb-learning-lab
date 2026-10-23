from datetime import datetime, timedelta, timezone
from pymongo import MongoClient

URI = "mongodb://labuser:labpassword@localhost:27017/?authSource=admin"


def main():
    client = MongoClient(URI)
    db = client["parcelflow"]

    for name in ["customers", "orders", "inventory", "events"]:
        db[name].delete_many({})

    now = datetime.now(timezone.utc)
    customers = [
        {"customerId": f"C-{i:04d}", "name": f"Customer {i}",
         "country": "IE" if i % 2 else "GB",
         "city": "Dublin" if i % 3 else "Cork"}
        for i in range(1, 101)
    ]
    inventory = [
        {"sku": f"SKU-{i:04d}", "name": f"Parcel item {i}",
         "available": 100 + (i % 20),
         "warehouse": "DUB-1" if i % 2 else "LON-1"}
        for i in range(1, 51)
    ]
    orders, events = [], []
    statuses = ["created", "packed", "in_transit", "delivered"]
    for i in range(1, 1001):
        created = now - timedelta(minutes=i)
        status = statuses[i % len(statuses)]
        order_id = f"ORD-{i:06d}"
        sku = f"SKU-{(i % 50) + 1:04d}"
        orders.append({
            "orderId": order_id,
            "customerId": f"C-{(i % 100) + 1:04d}",
            "status": status,
            "createdAt": created,
            "destination": {"country": "IE" if i % 2 else "GB",
                             "city": "Dublin" if i % 3 else "Cork"},
            "items": [{"sku": sku, "quantity": (i % 3) + 1,
                       "unitPrice": 19.99}],
            "payment": {"status": "authorized"},
        })
        events.append({"orderId": order_id, "eventType": status,
                       "createdAt": created,
                       "location": "Dublin" if i % 3 else "Cork"})

    db.customers.insert_many(customers)
    db.inventory.insert_many(inventory)
    db.orders.insert_many(orders)
    db.events.insert_many(events)

    print("Seeded ParcelFlow")
    for name in ["customers", "inventory", "orders", "events"]:
        print(f"{name}: {db[name].count_documents({})}")


if __name__ == "__main__":
    main()
