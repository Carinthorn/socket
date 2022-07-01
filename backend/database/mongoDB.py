import pymongo
import os
from dotenv import load_dotenv
load_dotenv()
client = pymongo.MongoClient(os.getenv('URI'))
database = client["chatapp"]

def getDatabase():
    return database
