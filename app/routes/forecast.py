from fastapi import APIRouter, Query, HTTPException
from app.services.stormglass_service import get_wave_forecast

router = APIRouter()

# Default coordinates (your location)
DEFAULT_LAT = 32.3775275
DEFAULT_LON = 34.8629629

@router.get("/")
async def forecast(
    lat: float = Query(DEFAULT_LAT, description="Latitude, optional"),
    lon: float = Query(DEFAULT_LON, description="Longitude, optional")
):
    """
    Returns the wave forecast for given coordinates.
    Defaults to your location if none are provided.
    """
    try:
        data = await get_wave_forecast(lat, lon)
        return {"latitude": lat, "longitude": lon, "forecast": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
