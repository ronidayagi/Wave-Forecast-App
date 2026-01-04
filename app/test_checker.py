import json
from datetime import datetime
from app.condition_checker import check_conditions

with open("Israel, beit yanai.json", "r") as f:
    forecast_data = json.load(f)

location_config = {
    "name": "Beit Yanai",
    "conditions": {
        "wave_height_min": 0.3,  # Lower so we find some matches
        "wave_height_max": 2.5,
        "wave_direction_min": 50,  # Wider range for testing
        "wave_direction_max": 150
    }
}

good_hours = check_conditions(forecast_data, location_config)

print(f"Found {len(good_hours)} good hours:")
for hour in good_hours:
    print(f"  - {hour['time']}: {hour['waveHeight']['noaa']}m, {hour['waveDirection']['noaa']}°")
