from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class SettingsApi(BaseSettings):

    

    API_V_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://postgres:root12345@localhost:5432/api-mtg"
    DBBaseModel = declarative_base()


    class Config:
        case_sensitive = True


settings = SettingsApi()