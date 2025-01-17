import os
import json
import logging
from typing import Dict, Any
from fastapi import Form, Depends, FastAPI, APIRouter, Request, HTTPException, Body  
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi import HTTPException, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from . import models, database
from .middleware import conf_dir
from .models import Conn, ConnCreate
from .database import SessionLocal
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from .connectors import get_connection_url

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

logger = logging.getLogger(__name__)

###m oved to main.py ###
# exception handler for model validation errors
# @app.exception_handler(RequestValidationError)
#
# @router.exception_handler(RequestValidationError)
# async def validation_exception_handler(request: Request, exc: RequestValidationError):
#     logger.error(f"Validation error: {exc.errors()}")
#     return JSONResponse(
#         status_code=422,
#         content={"detail": exc.errors()},
#     )


# routes
@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/connections", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("connections.html", {"request": request})


# @router.post("/crt-connection", response_model=ConnCreate)
# def create_connection(conn_data: ConnCreate, db: Session = Depends(get_db)):
#     db_conn = models.Conn(**conn_data.dict()) 
#     db.add(db_conn)
#     db.commit()
#     db.refresh(db_conn)
#     return db_conn
# modified to be specific for htmx

### works but encountered json mismatch validation issues
# @router.post("/crt-connection", response_class=HTMLResponse)
# async def create_connection(conn_data: ConnCreate, request: Request, db: Session = Depends(get_db)):
#     db_conn = models.Conn(**conn_data.dict()) 
#     db.add(db_conn)
#     db.commit()
#     db.refresh(db_conn)

#     return f"""
#     <li>{db_conn.name} - {db_conn.type} - {db_conn.host}:{db_conn.port} - SSL: {db_conn.ssl}</li>
#     """

@router.post("/crt-connection", response_class=HTMLResponse)
async def create_connection(
    request: Request,
    name: str = Form(...),
    type: str = Form(...),
    host: str = Form(...),
    port: int = Form(...),
    password: str = Form(...),
    ssl: bool = Form(False),  
    sid: str = Form(None),
    svc_name: str = Form(None),
    alt_conf: str = Form(None),
    description: str = Form(None),
    dsn: str = Form(None),  
    driver: str = Form(None),  
    db: Session = Depends(get_db)
):
    conn_data = {
        "name": name,
        "type": type,
        "host": host,
        "port": port,
        "password": password,
        "ssl": ssl,
        "sid": sid,
        "svc_name": svc_name,
        "alt_conf": alt_conf,
        "description": description,
        "dsn": dsn,  
        "driver": driver,  
    }

    print("Received connection data:", conn_data)

    db_conn = models.Conn(**conn_data)
    db.add(db_conn)
    db.commit()
    db.refresh(db_conn)

    return f"""
    <li>{db_conn.name} - {db_conn.type} - {db_conn.host}:{db_conn.port} - SSL: {db_conn.ssl}</li>
    """

@router.put("/update-connection", response_class=HTMLResponse)
async def update_connection(
    id: int = Form(...),
    name: str = Form(...),
    type: str = Form(...),
    host: str = Form(...),
    port: int = Form(...),
    password: str = Form(...),
    ssl: bool = Form(False),
    sid: str = Form(None),  
    svc_name: str = Form(None),  
    description: str = Form(None),
    dsn: str = Form(None),  
    driver: str = Form(None),  
    db: Session = Depends(get_db)
):
    try:
        db_conn = db.query(models.Conn).filter(models.Conn.id == id).first()
        if not db_conn:
            raise HTTPException(status_code=404, detail="Connection not found")

        db_conn.name = name
        db_conn.type = type
        db_conn.host = host
        db_conn.port = port
        db_conn.password = password
        db_conn.ssl = ssl
        db_conn.sid = sid  
        db_conn.svc_name = svc_name  
        db_conn.description = description
        db_conn.dsn = dsn  
        db_conn.driver = driver  

        db.commit()
        db.refresh(db_conn)

        return ""
    except Exception as e:
        print(f"Failed to update connection: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to update connection")

@router.get("/get-connections", response_class=HTMLResponse)
async def get_connections(request: Request, db: Session = Depends(get_db)):
    connections = db.query(models.Conn).all()
    connections_html = ""
    for conn in connections:
        connections_html += f"""
        <tr class="border-b dark:border-gray-700">
            <th scope="row" class="px-4 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white">{conn.name}</th>
            <td class="px-4 py-3">{conn.type}</td>
            <td class="px-4 py-3">{conn.host}</td>
            <td class="px-4 py-3">{conn.port}</td>
            <td class="px-4 py-3">{conn.description}</td>
            <td class="px-4 py-3 flex items-center justify-end">
                <button onclick="openEditModal(
                    {conn.id}, 
                    '{conn.name}', 
                    '{conn.type}', 
                    '{conn.host}', 
                    {conn.port}, 
                    '{conn.password}', 
                    {str(conn.ssl).lower()}, 
                    '{conn.description}', 
                    '{conn.sid}', 
                    '{conn.svc_name}', 
                    '{conn.dsn}', 
                    '{conn.driver}'
                )" class="inline-flex items-center p-0.5 text-sm font-medium text-center text-gray-500 hover:text-gray-800 rounded-lg focus:outline-none dark:text-gray-400 dark:hover:text-gray-100" type="button">
                    <svg class="w-5 h-5" aria-hidden="true" fill="currentColor" viewbox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                        <path d="M6 10a2 2 0 11-4 0 2 2 0 014 0zM12 10a2 2 0 11-4 0 2 2 0 014 0zM16 12a2 2 0 100-4 2 2 0 000 4z" />
                    </svg>
                </button>
            </td>
        </tr>
        """
    return connections_html

# reduced route complexity for index 
# didnt want to include a full set of details to pass to the page for no reason since we're
# just displaying the option's namne and type
@router.get("/get-connections-options", response_class=HTMLResponse)
async def get_connections_options(db: Session = Depends(get_db)):
    connections = db.query(models.Conn).all()
    options_html = ""
    for conn in connections:
        options_html += f'<option value="{conn.id}">{conn.name} - {conn.type}</option>'
    return options_html

    
@router.post("/run-sql")
async def run_sql(
    # payload: dict = Body(...),
    payload: Dict[str, Any] = Body(...),
    db: Session = Depends(get_db)
):
    query = payload.get("query")
    connection_id = payload.get("connection_id")

    if not query or not connection_id:
        raise HTTPException(status_code=400, detail="Query and connection ID are required.")

    conn = db.query(Conn).filter(Conn.id == connection_id).first()
    if not conn:
        raise HTTPException(status_code=404, detail="Connection not found.")

    try:
        connection_url = get_connection_url(conn)

        # SQLAlchemy engine
        engine = create_engine(connection_url)

        # Execute
        with engine.connect() as connection:
            result = connection.execute(text(query))

            # build other logic outside of select TBD like CTE's
            if query.strip().lower().startswith("select"):
                columns = result.keys()
                rows = result.fetchall()
                results = [dict(zip(columns, row)) for row in rows]
            else:
                results = {"message": "Query executed successfully."}

        return {"status": "success", "results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to execute query: {str(e)}")