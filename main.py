import os
from concurrent.futures import ProcessPoolExecutor

import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.config import Config
from starlette.middleware.sessions import SessionMiddleware
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Logging is configured correctly!")

# Custom module imports
from src.routes import router as main_router  # Import the router from routes.py

# Configure session secret
config = Config('.env')
SECRET_KEY = config('SECRET_KEY', cast=str, default='your-secret-key')

app = FastAPI() 
logging.basicConfig(level=logging.INFO)
app.add_middleware(SessionMiddleware, secret_key="some-random-secret-key")

# Register the router from routes.py
app.include_router(main_router)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Determine the number of available CPUs and use all but one
max_workers = max(1, os.cpu_count() - 1)
executor = ProcessPoolExecutor(max_workers=max_workers)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=30000)