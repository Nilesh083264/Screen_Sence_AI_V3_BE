from fastapi import FastAPI, HTTPException, Depends
import uvicorn
# from database import SessionLocal, engine, Base
from api.routes import router as api_routers
from core.config import settings
from utils.logger import *

logger = get_logger(__name__)
logger.info("Start Server:")

app = FastAPI()
app.include_router(api_routers)


if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.HOST, port=settings.PORT)
