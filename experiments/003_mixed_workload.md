# Experiment 003: Mixed OLTP and analytical workload

## Question
What happens when point updates and broad aggregations run together?

Run the checkout workload repeatedly in one terminal while running this aggregation in another:

```javascript
db.orders.aggregate([
  { $match: { createdAt: { $exists: true } } },
  { $unwind: "$items" },
  { $group: { _id: "$items.sku", quantity: { $sum: "$items.quantity" } } },
  { $sort: { quantity: -1 } }
], { allowDiskUse: true })
```

Record application latency before, during, and after the aggregation.
