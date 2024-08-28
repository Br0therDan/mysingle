# app/core/config.py

from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl, PostgresDsn, validator
from typing import List, Union
import os

class Settings(BaseSettings):
    APP_NAME: str = os.getenv("APP_NAME", "My Application")
    APP_ENV: str = os.getenv("APP_ENV", "development")
    APP_DEBUG: bool = os.getenv("APP_DEBUG", "True").lower() == "true"
    APP_VERSION: str = os.getenv("APP_VERSION", "0.1.0")

    # CORS settings
    CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:3000", "http://localhost:8000"]

    # Supabase settings
    SUPABASE_DATABASE_URL: Union[PostgresDsn, None] = None
    SUPABASE_URL: Union[AnyHttpUrl, None] = None
    SUPABASE_API_ANON_KEY: str = os.getenv("SUPABASE_API_ANON_KEY", "")
    SUPABASE_SERVICE_ROLE_SECRET: str = os.getenv("SUPABASE_SERVICE_ROLE_SECRET", "")
    SUPABASE_JWT_SECRET: str = os.getenv("SUPABASE_JWT_SECRET", "")
    SUPABASE_ACCESS_TOKEN_EXPIRE_MINUTES: int = 3600
    SUPABASE_JWT_ALGORITHM: str = "HS256"

    @validator("CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: str, values: dict) -> List[str]:
        if values.get("APP_ENV") == "production":
            return os.getenv("CORS_ORIGINS", "").split(",")
        return v or os.getenv("LOCAL_CORS_ORIGINS", "").split(",")

    @validator("SUPABASE_DATABASE_URL", pre=True, always=True)
    def set_database_url(cls, v, values):
        if values.get("APP_ENV") == "production":
            return os.getenv("SUPABASE_DATABASE_URL")
        return os.getenv("LOCAL_SUPABASE_DATABASE_URL")

    @validator("SUPABASE_URL", pre=True, always=True)
    def set_supabase_url(cls, v, values):
        if values.get("APP_ENV") == "production":
            return os.getenv("SUPABASE_URL")
        return os.getenv("LOCAL_SUPABASE_API_URL")

    @validator("SUPABASE_API_ANON_KEY", pre=True, always=True)
    def set_api_anon_key(cls, v, values):
        if values.get("APP_ENV") == "production":
            return os.getenv("SUPABASE_API_ANON_KEY", "")
        return v or os.getenv("LOCAL_SUPABASE_API_ANON_KEY", "")

    @validator("SUPABASE_SERVICE_ROLE_SECRET", pre=True, always=True)
    def set_service_role_secret(cls, v, values):
        if values.get("APP_ENV") == "production":
            return os.getenv("SUPABASE_SERVICE_ROLE_SECRET", "")
        return v or os.getenv("LOCAL_SUPABASE_SERVICE_ROLE_SECRET", "")

    @validator("SUPABASE_JWT_SECRET", pre=True, always=True)
    def set_jwt_secret(cls, v, values):
        if values.get("APP_ENV") == "production":
            return os.getenv("SUPABASE_JWT_SECRET", "")
        return v or os.getenv("LOCAL_SUPABASE_JWT_SECRET", "")

    @validator("SUPABASE_ACCESS_TOKEN_EXPIRE_MINUTES", pre=True, always=True)
    def set_access_token_expire_minutes(cls, v, values):
        if values.get("APP_ENV") == "production":
            return int(os.getenv("SUPABASE_ACCESS_TOKEN_EXPIRE_MINUTES", 3600))
        return int(os.getenv("LOCAL_SUPABASE_ACCESS_TOKEN_EXPIRE_MINUTES", 3600))

    @validator("SUPABASE_JWT_ALGORITHM", pre=True, always=True)
    def set_jwt_algorithm(cls, v, values):
        if values.get("APP_ENV") == "production":
            return os.getenv("SUPABASE_JWT_ALGORITHM", "HS256")
        return v or os.getenv("LOCAL_SUPABASE_JWT_ALGORITHM", "HS256")

    class Config:
        case_sensitive = True

settings = Settings()