import motor.motor_asyncio
import os
import pymongo


class DBHandler:
    def __init__(self):
        self.connection_string = os.getenv("MONGO_URL")

    def __enter__(self):
        self.client = motor.motor_asyncio.AsyncIOMotorClient(self.connection_string)
        self.db = self.client.url
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()


class MongoHandler:
    def __init__(self):
        self.connection_string = os.getenv("MONGO_URL")

    def __enter__(self):
        self.client = client = pymongo.MongoClient(
            self.connection_string, serverSelectionTimeoutMS=5000
        )
        self.db = self.client.url
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()
