# python -m pip install pymongo==3.11
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

user = os.getenv('MONGO_USER')
password = os.getenv('MONGO_PASSWORD')

uri = "mongodb+srv://{user}:{password}>@cluster0.blsgxxs.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)