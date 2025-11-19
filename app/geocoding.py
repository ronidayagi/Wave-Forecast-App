from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="my_app", timeout=10)
#location = geolocator.geocode("Israel, beit yanai")

def get_lat_lon(place_name):
    location = geolocator.geocode(place_name)
    if location:
        return location.latitude, location.longitude
    return None, None


