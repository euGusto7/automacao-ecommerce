import os
from dotenv import load_dotenv

if not os.path.exists(".env"):
    raise FileNotFoundError(
        "Arquivo .env não encontrado. Certifique-se de criar um arquivo .env com as variáveis necessárias."
    )

load_dotenv()


class Config:
    BASE_URL = os.getenv("BASE_URL")
    USERNAME = os.getenv("TEST_USERNAME")
    PASSWORD = os.getenv("TEST_PASSWORD")
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
