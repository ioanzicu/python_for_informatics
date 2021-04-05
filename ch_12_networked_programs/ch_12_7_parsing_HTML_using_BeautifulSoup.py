# 12.7 Parsing HTML using BeautifulSoup pg. 150

from urllib import request
from bs4 import BeautifulSoup

url = input('Enter - ')
html = request.urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # print(tag.get('href', None))

    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Content:', tag.contents[0])
    print('Attrs:', tag.attrs)
