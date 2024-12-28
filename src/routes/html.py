from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="src/html")

from src.frontend.WineBottle import WineBottle
router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def main_page(request: Request):
    wineBottles = WineBottle()
    wine = wineBottles.getBottle()
    try:
        return templates.TemplateResponse("index.html",{"request": request, "wine": wine})
    except FileNotFoundError:
        return HTMLResponse(content="File not found", status_code=404)

@router.get("/{wine}", response_class=HTMLResponse)
async def main_page(request: Request, wine: str):
    wineBottles = WineBottle()
    title = wineBottles.getWineTitel(wine)
    info = wineBottles.getInfo(wine)
    recommendation = wineBottles.getRecommendation(wine)
    try:
        return templates.TemplateResponse("wine.html",{"request": request, "wine": title, "info": info, "recommendation": recommendation, })
    except FileNotFoundError:
        return HTMLResponse(content="File not found", status_code=404)

