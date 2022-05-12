import uvicorn
from fastapi import FastAPI

from config.config import settings
from routes.api import api_router


app = FastAPI()

app = app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == '__main__':

    uvicorn.run("main:app", host="0.0.0.0", port=8000,log_level='info', reload=True)