# 5.2 pg. 57

# n = 5
# while n > 0:
#     print(n)
#     n = n-1
# else:
#     print('else after while')
# print('Blastoff!')


# BREAK 5.4 pg. 58

# while True:
#     line = input('> ')
#     if line == 'done':
#         break
#     print(line)

# print('Done!')


# CONTINUE 5.5 pg. 59

# while True:
#     line = input('> ')
#     if line[0] == '#':
#         continue
#     if line == 'done':
#         break
#     print(line)

# print('Done!')


# friends = ['Peter', 'Glenn', 'Joe']
# for friend in friends:
#     print('Happy New Year:', friend)
# print('Done!')


# Counting and summing loops 5.7.1 pg. 61
# COUNTING PATTERN

# count = 0
# for itervar in [3, 41, 12, 9, 74, 15]:
#     count = count + 1
# print('Count:', count)


# SUM NUMBERS PATTERN

# total = 0
# for itervar in [3, 41, 12, 9, 74, 15]:
#     total = total + itervar
# print('Total:', total)


# 5.7.2 Maximum and minimum loops pg. 62

# largest = None
# print('Before:', largest)

# for itervar in [3, 41, 12, 9, 74, 15]:
#     if largest is None or itervar > largest:
#         largest = itervar
#     print('Loop:', itervar, largest)
# print('Largest:', largest)


smallest = None
print('Before:', smallest)

for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print('Loop:', itervar, smallest)
print('Largest:', smallest)
