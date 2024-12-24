import os
from concurrent.futures import ProcessPoolExecutor
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.config import Config
from starlette.middleware.sessions import SessionMiddleware
import logging
from src.routes.html import router as html_router
from src.routes.app import router as app_router
# Logging configuration
app= FastAPI()
# Static files check
app.mount("/static", StaticFiles(directory="static"), name="static")
# HTML-Routen
app.include_router(html_router, prefix="")

# API-Routen
app.include_router(app_router, prefix="/app")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
