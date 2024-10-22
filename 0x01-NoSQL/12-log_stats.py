from pymongo import MongoClient
"""script that provides some stats about Nginx logs stored in MongoDB"""
client = MongoClient('mongodb://127.0.0.1:27017')
logs_collection = client.logs.nginx
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
all_logs = logs_collection.count_documents({})
print(f"{all_logs} logs")
print("Methods:")
for method in methods:
    numOfLogs = logs_collection.count_documents({"method": method})
    print(f"\tmethod {method}: {numOfLogs}")
statusMehtod = logs_collection.count_documents(
    {"method": "GET", "path": "status"}
    )
print(
    f"{statusMehtod} status check"
    )
