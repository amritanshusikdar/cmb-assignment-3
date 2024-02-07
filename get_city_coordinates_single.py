from geopy.geocoders import Nominatim

def get_lat_long(city_name):
    geolocator = Nominatim(user_agent="geo_locator")
    location = geolocator.geocode(city_name)
    if location:
        return location.latitude, location.longitude
    else:
        return None

def main():
    city_name = input("Enter the name of the city: ")
    coordinates = get_lat_long(city_name)
    if coordinates:
        latitude, longitude = coordinates
        print(f"The latitude and longitude of {city_name} are: {latitude}, {longitude}")
    else:
        print(f"Couldn't find coordinates for the city: {city_name}")

if __name__ == "__main__":
    main()
