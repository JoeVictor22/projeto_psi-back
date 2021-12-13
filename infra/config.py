from dotenv import load_dotenv
import os

load_dotenv()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
POR_PAGINA = 10
SQLALCHEMY_DATABASE_URI = os.getenv(
    "DATABASE", "postgresql://postgres:admin@localhost/banco_teste"
)
SQLALCHEMY_TRACK_MODIFICATIONS = True

JWT_SECRET_KEY = (
    "2d5issobnDGg2gyKfyvfb9gHRfUS23rysF6B14k3bgVnaFONmesmoH8JasodkmeuaAPdo2Chapaa23F"
)

DEBUG = True

print(f"\nStarting app with db={SQLALCHEMY_DATABASE_URI}\n")
