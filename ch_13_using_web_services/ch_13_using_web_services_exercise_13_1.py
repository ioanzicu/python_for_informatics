# Ex 13.1 pg. 167

# Change either the www.py4inf.com/code/geojson.py or www.py4inf.com/code/geoxml.py
# to print out the two-character country code from
# the retrieved data. Add error checking so your program does not traceback if the
# country code is not there. Once you have it working, search for “Atlantic Ocean”
# and make sure it can handle locations that are not in any country.

# I have used api.positionstack.com as google services are not free at the time being


import http.client
import urllib.parse
import json

try:
    conn = http.client.HTTPConnection('api.positionstack.com')
except Exception as err:
    print('Exception:', err)
    exit()

query = input('Enter location: ')

params = urllib.parse.urlencode({
    'access_key': ' ',  # ADD
    'query': query,
    'limit': 1,
})

try:
    conn.request('GET', '/v1/forward?{}'.format(params))
except Exception as err:
    print('Connection Exception:', err)
    exit()

try:
    res = conn.getresponse()
    data = res.read()
except Exception as err:
    print('Exception:', err)
    exit()

print(data.decode('utf-8'), end='\n\n')

try:
    js = json.loads(str(data, 'utf-8'))
except Exception as err:
    print('Deserialization Exception:', err)
    exit()


if not js['data']:
    print('JSON is empty! Invalid location:', query)
    exit()

lat = js['data'][0]['latitude']
lng = js['data'][0]['longitude']

print('Lat: ', lat)
print('Lng: ', lng)

location = js['data'][0]['label']
print('Loacation:', location)


if 'country' not in js['data'][0]:
    print('There is no country for location:', query)

country = js['data'][0]['country']
print('Country:', country)
