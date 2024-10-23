#!/usr/bin/env python3
"""script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


if __name__ == "__main__":
    """main script"""
    client = MongoClient("mongodb://127.0.0.1:27017")
    logs_collection = client.logs.nginx
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    all_logs = logs_collection.count_documents({})
    print(f"{all_logs} logs")
    print("Methods:")
    for method in methods:
        numOfLogs = logs_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {numOfLogs}")
    statusMehtod = logs_collection.count_documents(
        {"method": "GET", "path": "/status"}
        )
    print(f"{statusMehtod} status check")
    print("IPs:")
    ip_pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10},
    ]

    top_ips = logs_collection.aggregate(ip_pipeline)

    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")
