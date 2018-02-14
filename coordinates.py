import overpass
import requests

api_url = "https://maps.googleapis.com/maps/api/geocode/"
params = "json?address={address}&key={key}"
key = "AIzaSyC6rh33flbFuQUaKgU4uOP7u9SkSPO-AKU"


def get_latlong(address_list):
    return_list = []
    for address in address_list:
        result = requests.get(api_url + params.format(address=address, key=key))
        return_list.append(result.json()['results'][0]['geometry']['location'])

longs = return_list['latitude']
lats = return_list['latitude']

min_long = min(longs)
min_lat = min(lats)
max_long = max(longs)
max_lat = max(lats)

min_long-=0.5
min_lat-=0.5
max_long+=0.5
max_lat+=0.5


api = overpass.API()
map_query = overpass.MapQuery(min_lat,min_long,max_lat,max_long)
response = api.Get(map_query, responseformat="json")
print response