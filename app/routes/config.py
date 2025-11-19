from fastapi import APIRouter
from app.scheduler import place, update_daily_forecast

router = APIRouter()

@router.post("/set_place")
async def set_place(place1: str):
    global place
    place = place1
    #await update_daily_forecast()
    return {"message": "Place updated", "place": place}

@router.get("/place")
async def get_place():
    return {"place": place}
