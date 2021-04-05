# Ex 11.2 pg. 141

# Write a program to look for lines of the form
# New Revision: 39772
# and extract the number from each of the lines using a regular expression and the
# findall() method. Compute the average of the numbers and print out the average.

# Enter file:mbox.txt
# 38549.7949721
# Enter file:mbox-short.txt
# 39756.9259259

import re

fname = input('Enter file: ')
fhand = open(fname)

average = 0.0
total = 0.0
count = 0

for line in fhand:
    num = re.findall('New Revision: ([0-9]+)', line)
    if len(num) > 0:
        num = float(num[0])
        total += num
        count += 1

try:
    average = total / count
except ZeroDivisionError as err:
    print(err)
    exit()

print(average)
