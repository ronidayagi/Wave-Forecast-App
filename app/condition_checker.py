from datetime import datetime, timedelta

def check_conditions(forecast_data, location_config):
    tomorrow_date = (datetime.now() + timedelta(days=1)).date()

    # Filter to tomorrow's daylight hours only
    daylight_hours = [
        hour for hour in forecast_data["hours"]
        if 6 <= datetime.fromisoformat(hour["time"]).hour <= 15
           and datetime.fromisoformat(hour["time"]).date() == tomorrow_date
    ]
    # Get user's conditions
    conditions = location_config["conditions"]
    wave_height_min = conditions["wave_height_min"]
    wave_height_max = conditions["wave_height_max"]
    wave_direction_min = conditions["wave_direction_min"]
    wave_direction_max = conditions["wave_direction_max"]

    good_hours = []

    for hour in daylight_hours:
        wave_height = hour["waveHeight"]["noaa"]
        wave_direction = hour["waveDirection"]["noaa"]

        if (wave_height_min <= wave_height <= wave_height_max and
                wave_direction_min <= wave_direction <= wave_direction_max):
            good_hours.append(hour)

    return good_hours

def format_conditions_message(good_hours: list, location_name: str) -> str:
    if not good_hours:
        return "No good conditions found."

    message = f"🏄‍♂️ Good Surf Conditions at {location_name}!\n\n"
    message += f"Found {len(good_hours)} good hours tomorrow:\n\n"

    for hour in good_hours:
        time = datetime.fromisoformat(hour["time"]).strftime("%I:%M %p")
        wave_height = hour["waveHeight"]["noaa"]
        wave_direction = hour["waveDirection"]["noaa"]

        message += f"📅 {time}\n  Wave Height: {wave_height}m\n  Wave Direction: {wave_direction}°\n\n"

    message += "Go Surf!🌊"
    return message