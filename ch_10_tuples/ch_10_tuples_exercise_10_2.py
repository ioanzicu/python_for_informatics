# Ex 10.2 pg 127

# This program counts the distribution of the hour of the day for
# each of the messages. You can pull the hour from the “From” line by finding the
# time string and then splitting that string into parts using the colon character. Once
# you have accumulated the counts for each hour, print out the counts, one per line,
# sorted by hour as shown below.

# Sample Execution:
# python timeofday.py
# Enter a file name: mbox-short.txt
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1


fname = input('Enter a file name: ')

try:
    fhand = open(fname)
except:
    print('Cannot find file:', fname)
    exit()

hours_count = {}
for line in fhand:
    words = line.split()
    if len(words) > 5 and words[0] == 'From':
        time = words[5]
        hour, _, _ = time.split(':')
        hours_count[hour] = hours_count.get(hour, 0) + 1


# Decorate - dict to list of tuples
lst = list()
for hour, count in hours_count.items():
    lst.append((hour, count))

# Sort by first value
lst.sort()

# Undecorate - extract the data that we need
for hour, count in lst:
    print(hour, count)
