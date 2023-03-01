"""
 * file for sending the collected data to mongodb 
 * Created by Elias Vera-Jimenez
 * Last Updated March 1st, 2023
""" 

from dotenv import load_dotenv, find_dotenv
import os
import time

from pymongo import MongoClient
load_dotenv(find_dotenv()) # used to get the .env file.

password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://eliasrvjimenez:{password}@dfracsr.4ik124g.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)


db = client.DFRACSTwitterData
raw_data = db.RawData

def move_to_collection(tweet):
    raw_data.insert_one(tweet)


if __name__ == "__main__" :
    start = time.time()

    # Testing to see if the program can connect to mongodb
    try:
        print(client.server_info())
    except:
        print("connection error")


    print(time.time() - start, " elapsed.")
