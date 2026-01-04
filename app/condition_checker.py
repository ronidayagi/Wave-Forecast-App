from datetime import datetime

def check_conditions(forecast_data, location_config):

    # Filter to daylight hours
    daylight_hours = [hour for hour in forecast_data["hours"] if 6 <= datetime.fromisoformat(hour["time"]).hour <= 15 ]

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