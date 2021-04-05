# Ex 10.3 pg 128

# Write a program that reads a file and prints the letters in decreasing
# order of frequency. Your program should convert all the input to lower case and
# only count the letters a-z. Your program should not count spaces, digits, punctuation,
# or anything other than the letters a-z. Find text samples from several different
# languages and see how letter frequency varies between languages. Compare your
# results with the tables at wikipedia.org/wiki/Letter_frequencies.

import string

fname = input('Enter a file name: ')

try:
    fhand = open(fname)
except:
    print('Cannot find file:', fname)
    exit()

chars_count = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        for char in word:
            chars_count[char] = chars_count.get(char, 0) + 1
# print(letters_counts)


# Decorate - dict to list of tuples
lst = list()
for char, count in chars_count.items():
    lst.append((count, char))

# Sort by first value
lst.sort(reverse=True)

# Undecorate - extract the data that we need
for count, char in lst:
    print(char, count)
