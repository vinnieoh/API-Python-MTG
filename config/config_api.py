from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class SettingsApi(BaseSettings):

    

    API_V_STR: str = '/api/v1'
    #DB_URL: str = "postgresql+asyncpg://postgres:root12345@localhost:5432/api-mtg"
    DB_URL: str = "postgresql+asyncpg://nsjyfgacnyktzy:3c9fc73736724e6ca701a3b4cb09ce15c9a8208a33c14d0a5c0fe35da919bdf6@ec2-3-229-11-55.compute-1.amazonaws.com:5432/d66obtknp48ko2"
    DBBaseModel = declarative_base()


    class Config:
        case_sensitive = True


settings = SettingsApi()