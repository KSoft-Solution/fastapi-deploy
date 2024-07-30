import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v2"
    PROJECT_NAME: str = "Fastapi_Ecommerce"
    PROJECT_VERSION: str = "1.0.0"
    USE_SQLITE_DB: str = os.getenv("USE_SQLITE_DB")
    SQL_USER: str = os.getenv("SQL_USER")
    SQL_PASSWORD:str = os.getenv("SQL_PASSWORD")
    SQL_SERVER: str = os.getenv("SQL_SERVER", "localhost")
    SQL_PORT: str = os.getenv("SQL_PORT", 3306)
    SQL_DB: str = os.getenv("SQL_DB", "tdd")
    DATABASE_URL:str = os.getenv("DATABASE_URL")
    
    class Config:
        case_sensitive = True

settings = Settings()