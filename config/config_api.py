from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class SettingsApi(BaseSettings):

    

    API_V_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://ytffukfbzzlhko:d85f26510d9211ce7301345dc70c2966901fbc92520720c1849cc8bf93ba6f3b@ec2-54-172-175-251.compute-1.amazonaws.com:5432/d7fm7em29e7c6m"
    DBBaseModel = declarative_base()


    class Config:
        case_sensitive = True


settings = SettingsApi()