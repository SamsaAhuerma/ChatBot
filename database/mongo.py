from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")  # Guarda tu URI en un archivo .env
client = MongoClient(MONGO_URI)
db = client["cluster0"]
