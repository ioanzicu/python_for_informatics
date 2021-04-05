# 12.2 The World's Simplest Web Browser pg. 144

import socket
from urllib import request
import re


# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('www.data.pr4e.org', 80))
# mysock.send(b'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n')


# while True:
#     data = mysock.recv(1024)
#     if(len(data) < 1):
#         break
#     print(str(data, 'utf-8'))

# mysock.close()


# 12.3 Retreiving an image over HTTP pg. 145

# import socket
# import time

# HOST = 'data.pr4e.org'
# PORT = 80

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect((HOST, PORT))
# mysock.send(b'GET http://data.pr4e.org/cover.jpg HTTP/1.0\r\n\r\n')

# count = 0
# picture = b''

# while True:
#     data = mysock.recv(5120)
#     if (len(data) < 1):
#         break
#     time.sleep(0.25)
#     count = count + len(data)
#     print(len(data), count)
#     picture = picture + data

# mysock.close()

# # Look for the end of the header (2 CRLF)
# pos = picture.find(b'\r\n\r\n')
# print('Header length', pos)
# print(picture[:pos].decode())

# # Skip past the header and save the picture data
# picture = picture[pos+4:]
# fhand = open('./ch_12_networked_programs/stuff.jpg', 'wb')
# fhand.write(picture)
# fhand.close()


# 12.4 Retrieving web pages with urllib pg. 148


# fhand = request.urlopen('http://www.py4inf.com/code/romeo.txt')

# Print text
# for line in fhand:
#     line = str(line, 'utf-8')
#     print(line.strip())


# Count word's frequency
# counts = dict()
# for line in fhand:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
# print(counts)


# 12.6 Parsing HTML using regular expressions pg. 149

# url = input('Enter - ')
# html = request.urlopen(url).read()
# links = re.findall(b'href="(http://.*?)"', html)
# for link in links:
#     print(link.decode())


# 12.8 Reading binary files using urllib pg. 152

# img = request.urlopen('http://data.pr4e.org/cover.jpg')
# fhand = open('cover.jpg', 'wb')
# size = 0

# while True:
#     info = img.read(100000)
#     if len(info) < 1:
#         break
#     size = size + len(info)
#     fhand.write(info)

# print(size, 'characters copied.')
# fhand.close()
