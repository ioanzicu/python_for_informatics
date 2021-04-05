# Ex 12.5 pg. 154

# (Advanced) Change the socket program so that it only shows data
# after the headers and a blank line have been received. Remember that recv is
# receiving characters (newlines and all), not lines.


import socket
import re


def user_input():
    '''Returns a tuple of e elements: host and URL for connection'''
    while True:
        url = input('Enter URL: ')
        lst = url.split('/')
        if len(lst) >= 3:
            return (lst[2], url)

        print('URL should start with http://')


PORT = 80

host, url = user_input()
host = f'www.{host}'

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mysocket.connect((host, PORT))
except Exception as err:
    print(err)
    exit()

s = f'GET {url} HTTP/1.0\r\n\r\n'
mysocket.send(s.encode(encoding='UTF-8', errors='strict'))


response = ''

while True:
    data = mysocket.recv(1024)
    if not data:
        break
    response += str(data, 'utf-8')

mysocket.close()

blank_line = '\r\n\r\n'  # CRLF
response_list = response.split(blank_line, 1)

if len(response_list) >= 2:
    body = response_list[1]
    print(body)
