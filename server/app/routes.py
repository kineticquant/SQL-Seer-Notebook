from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi import HTTPException
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

# No longer passing themes to the API
# @router.get("/themes")
# async def read_themes():
#     try:
#         with open(cfg_file, "r") as cfg:
#             config = json.load(cfg)
#         return config.get("themes", []) 

#     except FileNotFoundError:
#         raise HTTPException(status_code=404, detail="Configuration JSON file not found.")
#     except json.JSONDecodeError:
#         raise HTTPException(status_code=500, detail="Error reading Configuration JSON file.")

#Post > Saving credentials
# Add to file