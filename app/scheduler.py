import asyncio
import json
from apscheduler.schedulers.background import BackgroundScheduler
from app.condition_checker import check_conditions, format_conditions_message
from app.config_loader import get_locations, get_user_email
from app.email_notifier import send_email
from app.services.stormglass_service import get_forecast  # your function
from app.geocoding import get_lat_lon
import datetime

async def update_forecast(place):

    lat, lon = get_lat_lon(place)

    print(f"Updating forecast for {place}: {datetime.datetime.now()}")

    forecast = await get_forecast(lat, lon)

    # Save forecast somewhere (file, DB, cache) so your API can serve it
    with open(f"{place}.json", "w") as f:
        json.dump(forecast, f, indent=4)
    print("Forecast updated!")

    return forecast

async def check_and_notify():
    print(f"\n🔍 Checking conditions: {datetime.datetime.now()}")

    locations = get_locations()
    user_email = get_user_email()

    for location in locations:
        lat = location["lat"]
        lon = location["lon"]
        forecast = await get_forecast(lat, lon)

        good_hours = check_conditions(forecast, location)

        if good_hours:
            message = format_conditions_message(good_hours, location["name"])
            send_email(user_email, f"🏄‍♂️ Good Surf at {location['name']}!", message)
        else:
            print(f"❌ {location['name']}: No good conditions")

def run_async_job():
    """Wrapper to run async function in scheduler"""
    asyncio.run(check_and_notify())

def start_scheduler():
    """Start the scheduler to check conditions periodically"""
    scheduler = BackgroundScheduler()

    # Run daily at 6am
    scheduler.add_job(run_async_job, 'cron', hour=6, minute=0)

    # Also run immediately on start
    scheduler.add_job(run_async_job, 'date', run_date=datetime.datetime.now())

    scheduler.start()
    print("📅 Scheduler started - checking every 6 hours")

