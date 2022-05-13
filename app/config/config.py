import os
from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class SettingsApi(BaseSettings):

    #user = os.environ.get('USER')
    #password = os.environ.get('PASSWORD')
    #db = os.environ.get('DB')
    #port = os.environ.get('PORT')


    API_V_STR: str = '/api/v1'
    #DB_URL: str = f"postgresql+asyncpg://{user}:{password}@localhost:{port}/{db}"
    DB_URL: str = "postgresql+asyncpg://postgres:root12345@localhost:5432/api-mtg"
    DBBaseModel = declarative_base()


    class Config:
        case_sensitive = True


settings = SettingsApi()