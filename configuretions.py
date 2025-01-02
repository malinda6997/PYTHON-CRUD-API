
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://malindaprabath876:ShC5tWbROkXpcltl@crud-api.jqorm.mongodb.net/?retryWrites=true&w=majority&appName=CRUD-API"

client = MongoClient(uri, server_api=ServerApi('1'))

db=client.todo_db
collection=db["todo_data"]