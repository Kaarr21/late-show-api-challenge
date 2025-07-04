import os
from dotenv import load_dotenv
load_dotenv()

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
SQLALCHEMY_TRACK_MODIFICATIONS = False
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
