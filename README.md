# MongoDB Learning Lab: ParcelFlow

This is the starter repository for the MongoDB bottom-up learning lab.

## Prerequisites

* Docker and Docker Compose
* Python 3.10+
* `pip install pymongo`
* `mongosh` (optional if using the Python scripts)

## Start the first lab

```bash
cd mongodb-learning-lab
docker compose -f docker/compose.single-node.yml up -d
python3 -m pip install pymongo
python3 seed/seed_parcelflow.py
python3 workloads/oltp_checkout.py
```

Connect manually with:

```bash
mongosh "mongodb://labuser:labpassword@localhost:27017/parcelflow"
```

Stop and remove the lab data with:

```bash
docker compose -f docker/compose.single-node.yml down -v
```

## Learning progression

1. Single node: CRUD, modeling, indexes, explain, profiling.
2. Replica set: replication, write concern, read preference, failover.
3. Sharded cluster: shard keys, targeted queries, scatter-gather, hotspots.
4. Mixed workloads: OLTP workload versus reporting workload.

The `experiments/` directory contains experiment prompts. Record predictions and observations instead of only copying commands.

## Important safety note

This lab is intentionally local and disposable. Do not bind it to a public interface or use production credentials.
