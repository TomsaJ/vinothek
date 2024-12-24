from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="src/templates")

@router.get("/", response_class=HTMLResponse)
async def main_page():
    return "<html><body><h1>Hallo world, willkommen bei der API!</h1></body></html>"

