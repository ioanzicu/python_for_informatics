# Ex 8.2 pg. 104

fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()

    if len(words) > 2 and words[0] == 'From':
        print(words[2])
