import os

class Config:
    SECRET_KEY = "your_secret_key"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:5432@localhost:5432/website"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
