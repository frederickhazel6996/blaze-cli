import motor.motor_asyncio
import os
from dotenv import load_dotenv


class DBHandler:
    def __init__(self):
        self.connection_string = os.getenv("MONGO_URL")

    def __enter__(self):
        self.client = motor.motor_asyncio.AsyncIOMotorClient(self.connection_string)
        self.db = self.client.valet
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()
