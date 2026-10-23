# Experiment 001: Baseline queries

## Question
What does a basic ParcelFlow workload look like before indexes or replication?

## Commands

```javascript
use parcelflow

db.orders.findOne({ orderId: "ORD-000001" })
db.orders.find({ status: "in_transit" }).limit(5)
db.orders.aggregate([
  { $group: { _id: "$status", count: { $sum: 1 } } }
])
```

## Observe

```javascript
db.orders.countDocuments()
db.orders.stats()
db.orders.getIndexes()
```

## Write down

* Which operations are point lookups?
* Which operation scans many documents?
* What indexes exist initially?
* What would become slow as the collection grows?
