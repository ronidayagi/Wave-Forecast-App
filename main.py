from fastapi import FastAPI
from app.routes.forecast import router as forecast_router
from app.routes.config import router as config_router
from app.scheduler import start_scheduler
from contextlib import asynccontextmanager

# Define lifespan FIRST
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Starting Surf Forecast App...")
    start_scheduler()
    yield
    print("👋 App shutting down")

# Then use it in FastAPI
app = FastAPI(title="Wave Forecast API", lifespan=lifespan)

# Health check endpoint
@app.get("/")
async def health_check():
    return {"status": "healthy", "service": "surf-forecast"}

# Include routers
app.include_router(forecast_router, prefix="/forecast")
app.include_router(config_router, prefix="/config")

# State variables (if you still need these)
#app.state.place = "Israel, beit yanai"
#app.state.forecast = None