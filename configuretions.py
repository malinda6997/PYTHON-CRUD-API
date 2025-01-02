import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch the MongoDB URI from the .env file
uri = os.getenv("MONGO_URI")

if not uri:
    raise ValueError("MONGO_URI not found in .env file")

# Create MongoDB client
client = MongoClient(uri, server_api=ServerApi('1'))

# Database and collection setup
db = client.todo_db
collection = db["todo_data"]
