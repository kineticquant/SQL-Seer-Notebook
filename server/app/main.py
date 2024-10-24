# connections.ini
# Preferred editor display

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Serve static files like CSS, JS, images
app.mount("/static", StaticFiles(directory="client/static"), name="static")

templates = Jinja2Templates(directory="client")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
