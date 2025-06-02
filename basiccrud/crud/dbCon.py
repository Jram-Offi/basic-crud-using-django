
from pymongo import MongoClient

client = MongoClient("mongodb+srv://Jramoffi:Jram20030517@cluster0.m6l5hio.mongodb.net/")
db = client["datas"]
col = db["users"]

# crud/dbCon.py