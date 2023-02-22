from dotenv import load_dotenv, find_dotenv
import os
import json

from pymongo import MongoClient
load_dotenv(find_dotenv()) # used to get the .env file.

password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://eliasrvjimenez:{password}@dfracsr.4ik124g.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)


production = client.DFRACSTwitterData
raw_production = production.RawData

