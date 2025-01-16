import os
import logging
from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .middleware import file_config, connections_config
from .routes import router
from . import database, models
from .database import SessionLocal

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Exception handler for validation errors
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Log the validation errors
    logger.error(f"Validation error: {exc.errors()}")
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors()},
    )

# Include the router
app.include_router(router)

# Create tables not yet existing
database.Base.metadata.create_all(bind=database.engine)

# db session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Mount static files
app.mount("/static", StaticFiles(directory="client/static"), name="static")
templates = Jinja2Templates(directory="client")

# Call middleware on startup to run setup procs
@app.on_event("startup")
async def startup_event():
    file_config()
    db = SessionLocal()
    try:
        connections_config(db)
    finally:
        db.close()