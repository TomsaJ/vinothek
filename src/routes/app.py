from fastapi import APIRouter

router = APIRouter()

@router.get("/api/greet/{name}")
async def greet_user(name: str):
    return {"message": f"Hallo {name}, willkommen bei der API!"}