#!/usr/bin/env python3

"""
Log stats from MongoDB nginx collection
"""

from pymongo import MongoClient


def log_stats():
    """
    Provides statistics on Nginx logs stored in MongoDB.
    Prints the total log count, counts for each HTTP method,
    and the count of status check logs.
    """
    client = MongoClient()
    collection = client.logs.nginx

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_count = collection.count_documents
    ({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")


if __name__ == "__main__":
    log_stats()
