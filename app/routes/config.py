from fastapi import APIRouter, Request
from app.scheduler import update_forecast

router = APIRouter()


@router.post("/set_place")
async def set_place(place1: str, request: Request):
    # access app.state via the Request object
    request.app.state.place = place1

    # optionally update forecast immediately
    request.app.state.forecast = await update_forecast(place1)

    return {"message": "Place updated", "place": request.app.state.place}


@router.get("/place")
async def get_place(request: Request):
    return {"place": request.app.state.place}
