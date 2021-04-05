# Ex 12.3 pg. 154

# Use urllib to replicate the previous exercise of (1) retrieving the
# document from a URL, (2) displaying up to 3000 characters, and (3) counting the
# overall number of characters in the document. Don’t worry about the headers for
# this exercise, simply show the first 3000 characters of the document contents.

from urllib import request


def user_input():
    '''Returns a tuple of e elements: host and URL for connection'''
    while True:
        url = input('Enter URL: ')
        lst = url.split('/')
        if len(lst) >= 3:
            return url

        print('URL should start with http://')


url = user_input()

try:
    web_resource = request.urlopen(url)
except Exception as err:
    print(str(err))
    exit()

count = 0
CHAR_LIMIT = 3000

while True:
    char = web_resource.read(1)
    if len(char) < 1 or count == CHAR_LIMIT:
        break
    count = count + len(char)
    print(str(char, 'utf-8'), count)

estimation = 'more than:' if count == CHAR_LIMIT else 'just:'
print('Total characters', estimation, count)
