# 8.1 A list is a sequence pg. 91

# cheeses = ['Cheddar', 'Edam', 'Gouda']
# numbers = [17, 123]
# empty = []

# print(cheeses, numbers, empty)


# 8.2 Lists are mutable pg. 91

# numbers = [17, 123]
# numbers[1] = 5
# print(numbers)

# print(5 in numbers)


# 8.3 Traversing a list pg. 92

# cheeses = ['Cheddar', 'Edam', 'Gouda']

# for cheese in cheeses:
#     print(cheese)


# numbers = [17, 123]

# for i in range(len(numbers)):
#     numbers[i] = numbers[i] * 2

# print(numbers)


# for x in []:
#     print('This never happens.')


# 8.4 List operations pg. 93

# a = [1, 2, 3]
# b = [4, 5, 6]

# c = a + b
# print(c)

# zeros = [0] * 4
# print(zeros)

# triple = [1, 2, 3] * 4
# print(triple)


# 8.5 List slices pg. 93

# t = ['a', 'b', 'c', 'd', 'e', 'f']
# print(t[1:3])
# print(t[:4])
# print(t[:3])
# print(t[:])

# t[1:3] = ['x', 'y']
# print(t)


# 8.6 List methods pg. 94

# t = ['a', 'b', 'c']
# t.append('d')
# print(t)


# t1 = ['a', 'b', 'c']
# t2 = ['d', 'e']
# t1.extend(t2)
# print(t1)
# print(t2)

# t = ['d', 'c', 'e', 'b', 'a']
# t.sort()
# print(t)

# # Methods are void - return None
# t = t.sort()
# print(t)


# 8.7 Deleting elements pg. 94

# t = ['a', 'b', 'c']
# x = t.pop(1)
# print(t)
# print(x)
# t.pop()
# print(t)


# t = ['a', 'b', 'c']
# del t[1]
# print(t)


# t = ['a', 'b', 'c']
# print(t.remove('b'))
# print(t)


# t = ['a', 'b', 'c', 'd', 'e', 'f']
# del t[1:5]
# print(t)


# 8.8 Lists and functions pg. 95

# nums = [3, 41, 12, 9, 74, 15]
# print(len(nums))
# print('Max: ', max(nums))
# print('Min: ', min(nums))
# print('Sum: ', sum(nums))
# print('Avg: ', sum(nums) / len(nums))


# total = 0
# count = 0
# while True:
#     inp = input('Enter a number: ')
#     if inp == 'done':
#         break
#     value = float(inp)
#     total = total + value
#     count = count + 1

# average = total / count
# print('Average: ', average)


# numlist = list()
# while True:
#     inp = input('Enter a number: ')
#     if inp == 'done':
#         break
#     value = float(inp)
#     numlist.append(value)

# average = sum(numlist) / len(numlist)
# print('Average: ', average)


# 8.9 Lists and strings pg. 96

# s = 'spam'
# t = list(s)
# print(t)

# s = 'pining for the fjords'
# t = s.split()
# print(t)
# print(t[2])


# s = 'spam-spam-spam'
# delimiter = '-'
# t = s.split(delimiter)
# print(t)


# t = ['pining', 'for', 'the', 'fjords']
# print(t)

# delimiter = ' '
# t = delimiter.join(t)
# print(t)


# 8.10 Parsing lines pg. 97

# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('From '):
#         continue

#     words = line.split()
#     print(words[2])


# 8.11 Objects and values pg. 98

# a = 'banana'
# b = 'banana'
# print(a is b)

# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a is b)


# 8.12 Aliasing pg. 99

# a = [1, 2, 3]
# b = a
# print(b is a)

# b[0] = 17
# print(a)


# 8.13 List arguments pg. 100

# def delete_head(t):
#     del t[0]


# letters = ['a', 'b', 'c']
# delete_head(letters)
# print(letters)


# # Modify existing list
# t1 = [1, 2]
# t2 = t1.append(3)
# print(t1)
# print(t2)


# # Create a new list
# t3 = t1 + [3]
# print(t3)
# print(t1 is t2)

# def bad_delete_head(t):
#     t = t[1:]  # Wrong!


# print(bad_delete_head([1, 2, 3, 4]))

# def tail(t):
#     return t[1:]  # OK!


# letters = ['a', 'b', 'c']
# rest = tail(letters)
# print(rest)


# 8.14 Debugging pg. 101

word = 'lol'
word = word.strip()  # OK!
# print(word)

t = [1, 2, 3, 4, 5, 6, 7]
# t = t.sort()    # WRONG!
# print(t)


# t.append('x')  # OK!
# print(t)
# t = t + ['x']  # OK!
# print(t)


# t.append(['x'])     # WRONG!
# print(t)
# t = t.append('x')   # WRONG!
# print(t)
# t + ['x']           # WRONG!
# print(t)
# t = t + 'x'         # WRONG!
# print(t)


fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()

    if len(words) == 0:
        continue

    if words[0] != 'From':
        continue

    if len(words) < 3:
        continue

    print(words[2])

#    if words and words[0] == 'From':
#         print(words[2])
