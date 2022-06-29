import requests
import folium
import json

with open('data\parsed\.json', 'r') as f:
    countries = json.load(f)
for country in countries:
    data = requests.get(
        f'http://api.worldbank.org/v2/country/{}/indicator/MS.MIL.XPND.GD.ZS?format=json&date=2013')
    print(data)
    
data = data.json()
for i in data[1]:
    id = i.get('countryiso3code')
    print(countries.get(id))
# print(data)

# m = folium.Map(location=[46.961580, -102.560670],
#                zoom_start=4)
# m.save('index.html')
