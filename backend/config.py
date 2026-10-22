import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    PORT = int(os.getenv("PORT", 5055))
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/foodrescue_db")
    DB_NAME = os.getenv("DB_NAME", "foodrescue_db")
    JWT_SECRET = os.getenv("JWT_SECRET", "supersecret_foodrescue_dev_key_2026_nosql")
    JWT_EXPIRATION_HOURS = int(os.getenv("JWT_EXPIRATION_HOURS", 24))
    ENV = os.getenv("FLASK_ENV", "development")
    DEBUG = ENV == "development"
