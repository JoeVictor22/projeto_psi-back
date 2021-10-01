from dotenv import load_dotenv
import os

load_dotenv()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SQLALCHEMY_DATABASE_URI = os.getenv(
    "DATABASE", "postgresql://postgres:admin@localhost/banco_teste"
)
SQLALCHEMY_TRACK_MODIFICATIONS = True

DEBUG = True

print(SQLALCHEMY_DATABASE_URI)
