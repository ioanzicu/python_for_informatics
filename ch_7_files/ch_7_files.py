# 7.2 Persistence pg. 80


# fhand = open('/mbox.txt')
# print(fhand)


# 7.3 Text files and lines pg. 81

# stuff = 'Hello\nWorld!'
# print(stuff)

# stuff = 'X\nY'
# print(stuff)

# print(len(stuff))


# 7.4 Reading files pg. 82

# fhand = open('/mbox.txt')
# count = 0

# for line in fhand:
#     count = count + 1

# print('Line Count:', count)


# inp = fhand.read()

# print(len(inp))
# print(inp[:20])


# 7.5 Searching through a file pg. 83

# for line in fhand:
#     line = line.rstrip()
#     # Skip 'uninteresting lines'
#     if not line.startswith('From:'):
#         continue
#     # Process out 'interesting' line
#     print(line)


# for line in fhand:
#     line = line.rstrip()
#     # Skip 'uninteresting lines'
#     if line.find('@uct.ac.za') == -1:
#         continue
#     # Process out 'interesting' line
#     print(line)


# 7.6 Letting the user choose the file name pg. 85

# fname = input('Enter the file name: ')
# fhand = open(fname)
# count = 0

# for line in fhand:
#     if line.startswith('Subject:'):
#         count = count + 1

# print('There were', count, 'subject lines in', fname)


# 7.7 Using try, except, and open pg. 85

# fname = input('Enter the file name: ')
# try:
#     fhand = open(fname)
# except:
#     print('File cannot be opened:', fname)
#     exit()

# count = 0
# for line in fhand:
#     if line.startswith('Subject:'):
#         count = count + 1

# print('There were', count, 'subject lines in', fname)


# 7.8 Writing files pg. 87

# fout = open('/output.txt', 'w')
# print(fout)

# line_1 = 'This here\'s the wattle,\n'
# fout.write(line_1)

# line_2 = 'the emblem of our land.\n'
# fout.write(line_2)

# fout.close()


# 7.9 Debugging pg. 87

a = '1 2\t 3\n 4'
print(a)
print(repr(a))
