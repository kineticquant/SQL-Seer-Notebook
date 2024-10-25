import os
import json
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi import HTTPException, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from . import models, database
from .middleware import conf_dir
from .models import Conn, ConnCreate
from .database import SessionLocal

router = APIRouter()

templates = Jinja2Templates(directory="client")

# db session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

cfg_file = os.path.join(conf_dir,'config.json')


# routes
@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/connections", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("connections.html", {"request": request})


@router.post("/crt-connection", response_model=ConnCreate)
def create_connection(conn_data: ConnCreate, db: Session = Depends(get_db)):
    db_conn = models.Conn(**conn_data.dict()) 
    db.add(db_conn)
    db.commit()
    db.refresh(db_conn)
    return db_conn