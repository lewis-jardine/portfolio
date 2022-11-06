import os
from dotenv import load_dotenv

from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:

  AZURE_API_KEY : str = os.getenv("AZURE_API_KEY")

  STORAGE_ACCOUNT_NAME: str = os.getenv("STORAGE_ACCOUNT_NAME")
  STORAGE_ACCOUNT_KEY: str = os.getenv("STORAGE_ACCOUNT_KEY")
  STORAGE_CONNECTION_STRING: str = os.getenv("STORAGE_CONNECTION_STRING")

settings = Settings()