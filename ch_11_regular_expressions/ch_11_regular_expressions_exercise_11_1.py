# Ex 11.1 pg. 140

# Write a simple program to simulate the operation of the grep command
# on Unix. Ask the user to enter a regular expression and count the number of
# lines that matched the regular expression:

# $ python grep.py
# Enter a regular expression: Author
# mbox.txt had 1798 lines that matched Author
# $ python grep.py
# Enter a regular expression: Xmbox.
# txt had 14368 lines that matched X-
# $ python grep.py
# Enter a regular expression: java$
# mbox.txt had 4218 lines that matched java$

import re

regex = input('Enter a regular expression: ')

fhand = open('./files/mbox.txt')

count = 0
for line in fhand:
    if re.findall(regex, line):
        count += 1

print(f'mbox.txt had {count} lines that matched {regex}')
