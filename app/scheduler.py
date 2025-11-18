import asyncio
import json
from apscheduler.schedulers.background import BackgroundScheduler
from app.services.stormglass_service import fetch_forecast  # your function
import datetime

async def update_daily_forecast():
    print(f"Updating forecast: {datetime.datetime.now()}")
    lat, lon = 32.3775275, 34.8629629  # choose your location

    forecast = await fetch_forecast(lat, lon)

    # Save forecast somewhere (file, DB, cache) so your API can serve it
    with open("forecast_cache.json", "w") as f:
        json.dump(forecast, f)
    print("Forecast updated!")

def start_scheduler():
    scheduler = BackgroundScheduler()
    # Schedule job to run every day at 6am
    scheduler.add_job(update_daily_forecast, 'cron', hour=6, minute=0)
    scheduler.start()
