# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.
import csv

class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon
    def __str__(self):
        return f"Name: {self.name} Latitude: {self.lat} Longitude: {self.lon}\n"

# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# Use Python's built-in "csv" module to read this file so that each record is
# imported into a City instance. (You're free to add more attributes to the City
# class if you wish, but this is not necessary.) Google "python 3 csv" for
# references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
raw_cities = []
with open('cities.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='/')
    for row in reader:
        raw_cities.append(row)

cities = []
for city in raw_cities[1:]:
    city_info = city[0].split(',')
    print(city_info)
    name, lat, lon = city_info[0], city_info[3], city_info[4]
    cities.append(City(name, lat, lon))

# Print the list of cities (name, lat, lon), 1 record per line.
for city in cities:
    print(city)

# Assumes that user enters only valid lats and lons, no strings
def getLocations():
    lat1, lon1 = input("Enter lat1, lon1: ").split(",")
    print(lat1, lon1)
    
    lat2, lon2 = input("Enter lat2, lon2: ").split(",")
    print(lat2, lon2)

    lat_min, lat_max = min(lat1, lat2), max(lat1, lat2)
    lon_min, lon_max = min(lon1, lon2), max(lon1, lon2)

    cities_within_square = [city for city in cities if lat_min <= city.lat <= lat_max and lon_min <= city.lon <= lon_max]
    
    for city in cities_within_square:
        print(city)


# *** STRETCH GOAL! ***
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Output the cities that fall
# within this square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO