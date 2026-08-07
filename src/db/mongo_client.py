"""
MongoDB client initialization.
"""

from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb+srv://shamshad1924138:UXSFDMWzsWPffRZR@cluster0.uzfcu.mongodb.net/"
DB_NAME = "adaptive_rag"

client = AsyncIOMotorClient(MONGO_URL)
db = client[DB_NAME]
