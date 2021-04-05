# Ex 12.1 pg. 153

# Change the socket program socket1.py to prompt the user for the
# URL so it can read any web page. You can use split(’/’) to break the URL into
# its component parts so you can extract the host name for the socket connect call.
# Add error checking using try and except to handle the condition where the user
# enters an improperly formatted or non-existent URL.

import socket


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

while True:
    data = mysocket.recv(1024)
    if len(data) < 1:
        break
    data = str(data, 'utf-8')
    print(data)

mysocket.close()
