import os
import logging
from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .middleware import file_config
from .routes import router
from . import database, models

app = FastAPI()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app.include_router(router)


# Create the database tables
database.Base.metadata.create_all(bind=database.engine)

# db session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
        logger.info("Connected to database successfully.")
    finally:
        db.close()
        

app.mount("/static", StaticFiles(directory="client/static"), name="static")
templates = Jinja2Templates(directory="client")

# call middleware on startup to run proc
@app.on_event("startup")
async def startup_event():
    file_config()
    

