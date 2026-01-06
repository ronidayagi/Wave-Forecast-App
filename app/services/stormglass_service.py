import httpx
import os
from fastapi import HTTPException
from dotenv import load_dotenv
load_dotenv()


API_KEY = os.getenv("STORMGLASS_API_KEY")
BASE_URL = "https://api.stormglass.io/v2/weather/point"

async def get_forecast(lat: float, lon: float):
    params = {
        "lat": lat,
        "lng": lon,
        "params": "waveHeight,waveDirection,wavePeriod,waterTemperature",
        "source": "noaa"
    }
    headers = {"Authorization": API_KEY} if API_KEY else {}

    try:
        async with httpx.AsyncClient(timeout=15) as client:
            response = await client.get(BASE_URL, params=params, headers=headers)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=f"StormGlass error: {e.response.text}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")


# DEBUG: Print ALL environment variables
print("=" * 50)
print("🔍 ALL ENVIRONMENT VARIABLES:")
for key, value in os.environ.items():
    if 'KEY' in key or 'API' in key or 'STORM' in key:
        print(f"  {key} = {value[:10]}..." if len(value) > 10 else f"  {key} = {value}")
print("=" * 50)

API_KEY = os.getenv("STORMGLASS_API_KEY")