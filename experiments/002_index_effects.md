# Experiment 002: Index effects

## Question
How does an index change the amount of work MongoDB performs?

## Before

```javascript
db.orders.find({ customerId: "C-0042" }).explain("executionStats")
```

## Change one variable

```javascript
db.orders.createIndex({ customerId: 1 })
```

## After

```javascript
db.orders.find({ customerId: "C-0042" }).explain("executionStats")
```

Compare `COLLSCAN` versus `IXSCAN`, `totalDocsExamined`, `totalKeysExamined`, and execution time.
