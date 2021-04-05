# 13.2 Parsing XML pg. 156

import xml.etree.ElementTree as ET

# data = '''
# <person>
#     <name>Chuck</name>
#     <phone type="int1">
#         +1 734 303 4456
#     </phone>
#     <email hide="yes"/>
# </person>'''

# tree = ET.fromstring(data)
# print('Name:', tree.find('name').text)
# print('Attr:', tree.find('email').get('hide'))


# 13.3 Looping through nodes pg. 156

# input = '''
# <stuff>
#     <users>
#         <user x="2">
#             <id>001</id>
#             <name>Chuck</name>
#         </user>
#         <user x="7">
#             <id>009</id>
#             <name>Brent</name>
#         </user>
#     </users>
# </stuff>'''

# stuff = ET.fromstring(input)
# lst = stuff.findall('users/user')
# print('User count:', len(lst))

# for item in lst:
#     print('Name', item.find('name').text)
#     print('Id', item.find('id').text)
#     print('Attribute', item.get('x'))


# 13.5 Parsing JSON pg. 158


# import json

# data = '''
# [
#     {
#         "id":"001",
#         "x": "2",
#         "name": "Chuck"
#     },
#     {
#         "id":"009",
#         "x":"7",
#         "name":"Brent"
#     }
# ]'''

# info = json.loads(data)
# print('User count:', len(info))

# for item in info:
#     print('Name', item['name'])
#     print('Id', item['id'])
#     print('Attribute', item['x'])


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
