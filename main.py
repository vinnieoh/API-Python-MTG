import uvicorn
from fastapi import FastAPI

from config.config_api import settings
from routes.api_config import api_router


app = FastAPI()

app.include_router(api_router, prefix=settings.API_V_STR)

# prefix => http://127.0.0.1:8000/api/v1/



if __name__ == '__main__':

    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level='info', reload=True)