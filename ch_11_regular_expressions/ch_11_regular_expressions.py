# 11 Regular Expressions pg. 129

import re

# fhand = open('./files/mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if re.search('^From:', line):
#         print(line)


# 11.1 Character matching in regular expressions pg. 130

# fhand = open('./files/mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if re.search('^F..m:', line):
#         print(line)

# . any character
# * zero or more characters
# + one or more characters
# .+ any character more than one

# fhand = open('./files/mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if re.search('^From:.+@', line):
#         print(line)


# 11.2 Extracting data using regular expressions pg. 131


# s = 'Hello from csev@umich.edu to cwen@iupui.edu about  the meeting @2PM'
# lst = re.findall('\S+@\S+', s)
# print(lst)


# fhand = open('./files/mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
#     if len(x) > 0:
#         print(x)


# 11.3 Combining searching and extracting pg. 133


# fhand = open('./files/mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if re.findall('^X\S*: [0-9.]+', line):
#         print(line)


# fhand = open('./files/mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     x = re.findall('^X\S*: ([0-9.]+)', line)
#     if len(x) > 0:
#         print(x)


# fhand = open('./files/mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     x = re.findall('^Details:.*rev=([0-9.]+)', line)
#     if len(x) > 0:
#         print(x)


# fhand = open('./files/mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     x = re.findall('^From .* ([0-9][0-9]):', line)
#     if len(x) > 0:
#         print(x)


# 11.4 Escape character pg. 137


# x = 'We just received $10.00 for cookies.'
# y = re.findall('\$[0-9.]+', x)
# print(y)


# 11.5 Summary pg.137

# ^          - beginning of the line
# $          - end of the line
# .          - any character(a wildcard)
# \s         - whitespace character
# \S         - non-whitespace character(opposite of \s)
# *          - zero or more characters
# *?         - zero or more characters in "non-gready mode"
# +          - one or more characters
# +?         - one or more characters in "non-gready mode"
# [aeiou]    - match a single character from specified set
# [a-z0-9]   - range of characters, match a lowercase letter or digit
# [^A-Za-z]  - a caret sign in the set notation inverts the logic. Any character
#              except the uppercase or lowercase letter
# ( )        - are ignored for the purpose of matching, allow to extract a particular
#              subset of the matched string but not the whole string
# \b         - empty string, only at the start or end of a word
# \B         - empty string, only NOT at the start or end of a word
# \d         - any decimals digit, equivalent to the set [0-9]
# \D         - any non-digit character, equivalent to the set [^0-9]
