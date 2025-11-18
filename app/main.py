from fastapi import FastAPI
from app.routes.forecast import router as forecast_router
from app.scheduler import start_scheduler, update_daily_forecast
from contextlib import asynccontextmanager
import asyncio

app = FastAPI(title="Wave Forecast API")
app.include_router(forecast_router, prefix="/forecast")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code
    print("Fetching initial forecast...")
    await update_daily_forecast()  # Run initial fetch

    start_scheduler()  # Start the daily scheduler
    print("Scheduler started")
    yield
    # Optional shutdown code
    print("App shutting down")

app.router.lifespan_context = lifespan

