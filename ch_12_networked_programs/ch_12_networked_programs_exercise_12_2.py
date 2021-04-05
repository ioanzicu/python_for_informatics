# Ex 12.2 pg. 153


# Change your socket program so that it counts the number of characters
# it has received and stops displaying any text after it has shown 3000 characters.
# The program should retrieve the entire document and count the total number
# of characters and display the count of the number of characters at the end of the
# document.

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

count = 0
CHAR_LIMIT = 3000

while True:
    char = mysocket.recv(1)
    if len(char) < 1 or count == CHAR_LIMIT:
        break
    count = count + len(char)
    print(str(char, 'utf-8'), count)

estimation = 'more than:' if count == CHAR_LIMIT else 'just:'
print('Total characters', estimation, count)

mysocket.close()
