import os
from contextlib import nullcontext
from typing import Optional

from fastapi import APIRouter, Request, Form, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import JSONResponse

from src.backend.Database import Database

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

@router.get("/newWine", response_class=HTMLResponse)
async def addNewWine(request: Request):
    try:
        return templates.TemplateResponse("newWine.html",{"request": request})
    except FileNotFoundError:
        return HTMLResponse(content="File not found", status_code=404)

@router.post("/addnewWine", response_class=HTMLResponse)
async def addNewWine(request: Request,
wineArt: str = Form(...),
    winename: str = Form(...),
    producer: str = Form(...),
    country: str = Form(...),
    vintageYear: str = Form(...),
    alcoholContent: Optional[float] = Form(None),  # Optionales Feld
    dekrantieren: Optional[str] = Form(None),      # Optionales Feld
    temp: Optional[str] = Form(None),              # Optionales Feld
    rec: Optional[str] = Form(None),               # Optionales Feld
    trockensueß: Optional[int] = Form(None),       # Optionales Feld
    leichtkraeftig: Optional[int] = Form(None),    # Optionales Feld
    flexibelTranninhalt: Optional[int] = Form(None), # Optionales Feld
    sanftSaeure: Optional[int] = Form(None),       # Optionales Feld
    image: Optional[UploadFile] = File(None)
):
    # Daten verarbeiten
    print(f"Weinart: {wineArt}")
    print(f"Weinname: {winename}")
    print(f"Hersteller: {producer}")
    print(f"Land: {country}")
    print(f"Jahrgang: {vintageYear}")
    print(f"Alkoholgehalt: {alcoholContent}")
    print(f"Dekantieren: {dekrantieren}")
    print(f"Temperatur: {temp}")
    print(f"Empfehlung: {rec}")
    print(f"Trocken/Süß: {trockensueß}")
    print(f"Leicht/Kräftig: {leichtkraeftig}")
    print(f"Flexibel/Tanninhalt: {flexibelTranninhalt}")
    print(f"Sanft/Säure: {sanftSaeure}")


    # Datei speichern (optional)
    if image is not None and len(await image.read()) > 0:
        # Bilddatei wurde hochgeladen
        upload_dir = "static/resource/wine-bottle/custom"
        os.makedirs(upload_dir, exist_ok=True)  # Erstelle den Ordner, falls er nicht existiert
        file_path = os.path.join(upload_dir, image.filename)
        with open(file_path, "wb") as buffer:
            buffer.write(await image.read())
        print(f"Hochgeladenes Bild: {image.filename}")
    response_data = {
        "message": "Daten erfolgreich empfangen",
        "wineArt": wineArt,
        "winename": winename,
        "producer": producer,
        "country": country,
        "vintageYear": vintageYear,
        "alcoholContent": alcoholContent,
        "dekrantieren": dekrantieren,
        "temp": temp,
        "rec": rec,
        "trockensueß": trockensueß,
        "leichtkraeftig": leichtkraeftig,
        "flexibelTranninhalt": flexibelTranninhalt,
        "sanftSaeure": sanftSaeure,
        "image_filename": image.filename if image else None,
    }

    # Verwende JSONResponse, um sicherzustellen, dass das Dictionary als JSON zurückgegeben wird
    return JSONResponse(content=response_data)

@router.get("/{wine}", response_class=HTMLResponse)
async def mainPageWithWine(request: Request, wine: str):
    wineBottles = WineBottle()
    title = wineBottles.getWineTitel(wine)
    info = wineBottles.getInfo(wine)
    tasteCharacteristics = wineBottles.getTasteCharacteristics(wine)
    recommendation = wineBottles.getRecommendation(wine)
    try:
        return templates.TemplateResponse("wine.html",{"request": request, "wine": title, "info": info, "recommendation": recommendation, "tasteCharacteristics": tasteCharacteristics })
    except FileNotFoundError:
        return HTMLResponse(content="File not found", status_code=404)

