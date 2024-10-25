from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi import HTTPException, Depends
from fastapi.templating import Jinja2Templates
from .middleware import conf_dir

import os
import json

router = APIRouter()

templates = Jinja2Templates(directory="client")

cfg_file = os.path.join(conf_dir,'config.json')

@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/connections", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("connections.html", {"request": request})

#Post > Saving credentials
# Add to file