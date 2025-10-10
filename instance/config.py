import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'fallbacksecret')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///floral.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
