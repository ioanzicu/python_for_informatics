# Ex 12.4 pg. 154

# Change the urllinks.py program to extract and count paragraph
# (p) tags from the retrieved HTML document and display the count of the paragraphs
# as the output of your program. Do not display the paragraph text, only
# count them. Test your program on several small web pages as well as some larger
# web pages.

from urllib import request
from bs4 import BeautifulSoup

url = input('Enter - ')
try:
    html = request.urlopen(url).read()
except Exception as err:
    print('Error', err)

soup = BeautifulSoup(html, features="html.parser")

# Retrieve all of the anchor tags
tags = soup('p')
print(f'Total paragraphs:', len(tags))
