from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os


router = APIRouter()

templates = Jinja2Templates(directory="page")
UPLOAD_DIRECTORY = "uploads"
PATH_SEPARATOR = '\\' if os.name == 'nt' else '/'

@router.get("/{name}", response_class=HTMLResponse)
async def main_page(name: str):
    return {"message": f"Hallo {name}, willkommen bei der API!"}
    
@router.get("/api/greet/{name}")
async def greet_user(name: str):
    return {"message": f"Hallo {name}, willkommen bei der API!"}
