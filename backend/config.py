import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///nyc_taxi.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False