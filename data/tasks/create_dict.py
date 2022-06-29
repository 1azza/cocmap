import csv
import json
countries = {}
with open(r'data\raw\countries_codes_and_coordinates.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='"', quotechar='|')
    for row in reader:
        alpha2 = row["Alpha-2 code"]
        lat = row["Latitude (average)"]
        long = row["Longitude (average)"]
        countries[alpha2] = {
            "long" : float(long),
            "lat" : float(lat),
            "iso" : alpha2
        }
with open('data\parsed\.json', 'w') as f:
    json.dump(countries, f)
