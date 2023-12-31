# python -m pip install pymongo==3.11
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

from pymongo.server_api import ServerApi

load_dotenv()


class MongoConnection:
    def __init__(self):
        user = os.getenv('MONGO_USER')
        password = os.getenv('MONGO_PASSWORD')
        host = os.getenv('MONGO_HOST')
        uri = f"mongodb+srv://{user}:{password}@{host}/?retryWrites=true&w=majority"

        # Create a new client and connect to the server
        self.client = MongoClient(uri, server_api=ServerApi('1'))

    def test_connection(self):
        # Send a ping to confirm a successful connection
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    MongoConnection().test_connection()
