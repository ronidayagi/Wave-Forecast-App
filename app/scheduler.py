import asyncio
import json
from apscheduler.schedulers.background import BackgroundScheduler
from app.services.stormglass_service import get_forecast  # your function
from app.geocoding import get_lat_lon
import datetime

#place = "Israel, beit yanai"  # default

async def update_forecast(place):

    lat, lon = get_lat_lon(place)

    print(f"Updating forecast for {place}: {datetime.datetime.now()}")

    forecast = await get_forecast(lat, lon)

    # Save forecast somewhere (file, DB, cache) so your API can serve it
    with open(f"{place}.json", "w") as f:
        json.dump(forecast, f, indent=4)
    print("Forecast updated!")

    return forecast

def start_scheduler():
    scheduler = BackgroundScheduler()
    # Schedule job to run every day at 6am
    scheduler.add_job(update_forecast, 'cron', hour=6, minute=0)
    scheduler.start()

