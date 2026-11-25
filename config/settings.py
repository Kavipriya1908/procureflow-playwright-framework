import os
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

BASE_URL = os.getenv("BASE_URL")
API_BASE_URL = os.getenv("API_BASE_URL")
VALID_EMAIL = os.getenv("VALID_EMAIL")
VALID_PASSWORD = os.getenv("VALID_PASSWORD")


def has_credentials():
    return bool(VALID_EMAIL and VALID_PASSWORD)