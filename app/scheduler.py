import asyncio
import json
from apscheduler.schedulers.background import BackgroundScheduler
from app.services.stormglass_service import fetch_forecast  # your function
from app.geocoding import get_lat_lon
import datetime

place = "Israel, beit yanai"  # default

async def update_daily_forecast():

    lat, lon = get_lat_lon(place)

    print(f"Updating forecast for {place}: {datetime.datetime.now()}")

    forecast = await fetch_forecast(lat, lon)

    # Save forecast somewhere (file, DB, cache) so your API can serve it
    with open("forecast_cache.json", "w") as f:
        json.dump(forecast, f, indent=4)
    print("Forecast updated!")

def start_scheduler():
    scheduler = BackgroundScheduler()
    # Schedule job to run every day at 6am
    scheduler.add_job(update_daily_forecast, 'cron', hour=6, minute=0)
    scheduler.start()

