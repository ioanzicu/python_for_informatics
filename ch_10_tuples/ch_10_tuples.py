# 10.1 Tuples are immutable pg. 117

# t = 'a', 'b', 'c', 'd', 'e'  # legal tuple
# t = ('a', 'b', 'c', 'd', 'e')
# t = ('a',)  # tuple
# # t = ('a') # string
# print(t)
# print(type(t))


# t = tuple()
# print(t)

# t = tuple('lupins')
# print(t)

# t = ('a', 'b', 'c', 'd', 'e')
# print(t[0])
# print(t[1:3])

# t[0] = 'A' # ILEGAL!

# t = ('A',) + t[1:]  # create a new tuple
# print(t)


# 10.2 Comparing tuples pg. 118


# print((0, 1, 2) < (0, 3, 4))
# print((0, 1, 20000) < (0, 3, 4))


# DSU Pattern

# txt = 'but soft what light in yonder window breaks'
# words = txt.split()

# # Decorate - build a list of tuples
# t = list()
# for word in words:
#     t.append((len(word), word))

# # Sort
# t.sort(reverse=True)

# # Undecorate - extract the sorted elements
# res = list()
# for length, word in t:
#     res.append(word)

# print(res)


# 10.3 Tuple assignment pg. 119


# m = ['have', 'fun']
# # x, y = m  # tuple assignmen without braces
# (x, y) = m
# print(x, y)


# swap

# a = 1
# b = 2
# print(a, b)
# a, b = b, a  # left side - tuple of variables, right side - tuple of expressions
# print(a, b)


# addr = 'monty@python.org'

# uname, domain = addr.split('@')
# print(uname, domain)


# 10.4 Dictionaries and tuples pg. 121

# d = {'c': 22, 'a': 10, 'b': 1}
# t = d.items()
# print(t)
# t = list(t)
# t.sort()
# print(t)
# t = dict(t)
# print(t)


# 10.5 Multiple assignment with dictionaries pg. 121

# d = {'c': 22, 'a': 10, 'b': 1}
# for key, val in d.items():
#     print(val, key)


# d = {'c': 22, 'b': 1, 'a': 10}
# l = list()
# for key, val in d.items():
#     l.append((val, key))

# print(l)
# l.sort(reverse=True)
# print(l)


# 10.6 The most common words pg. 122

# import string
# fhand = open('romeo-full.txt')

# counts = dict()
# for line in fhand:
#     line = line.translate(str.maketrans('', '', string.punctuation))
#     line = line.lower()
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1

# # Sort the dictionary by value
# lst = list()
# for k, v in counts.items():
#     lst.append((v, k))

# lst.sort(reverse=True)

# for k, v in lst[:10]:
#     print(k, v)


# 10.7 Using tuples as keys in dictionaries pg. 124

# directory = {}
# directory['John', 'Doe'] = '121345'
# directory['Jey', 'Doe'] = '543212'

# for last, first in directory:
#     print(last, first, directory[last, first])
