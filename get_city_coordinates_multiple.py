from geopy.geocoders import Nominatim

def get_lat_long(city_name):
    geolocator = Nominatim(user_agent="geo_locator")
    location = geolocator.geocode(city_name, exactly_one=False)  # Setting exactly_one to False to allow multiple results
    if location:
        coordinates = [(result.latitude, result.longitude) for result in location]
        return coordinates
    else:
        return None

def main():
    city_name = input("Enter the name of the city: ")
    coordinates = get_lat_long(city_name)
    if coordinates:
        print(f"The latitude and longitude of {city_name} are:")
        for i, (latitude, longitude) in enumerate(coordinates, start=1):
            print(f"{i}. {latitude}, {longitude}")
    else:
        print(f"Couldn't find coordinates for the city: {city_name}")

if __name__ == "__main__":
    main()
