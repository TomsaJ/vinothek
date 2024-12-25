from fastapi import APIRouter

from src.backend.Database import Database

router = APIRouter()
db = Database()

@router.get("/api/greet/{name}")
async def greet_user(name: str):
    return {"message": f"Hallo {name}, willkommen bei der API!"}

@router.get("/api/getWine")
async def greet_user():
    try:
        # Fetch all wines
        vino = db.getAllWines()
        # Join all the first column values into a single string
        vino = ''.join([
            "Kategorie: " + str(x[2]) + " | " + "Name: " + str(x[5]) + "\n"
            for x in vino
        ])
        return {"message": vino}

    except Exception as e:
        # Handle errors gracefully
        return {"error": str(e)}

