# 9 Dictionaries pg. 107

import string

eng_2_sp = dict()
# print(eng_2_sp)

eng_2_sp['one'] = 'uno'
# print(eng_2_sp)

eng_2_sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
# print(eng_2_sp)
# print(eng_2_sp['two'])
# print(eng_2_sp['four'])  # Exception!
# print(len(eng_2_sp))

# print('one' in eng_2_sp)  # keys
# print('uno' in eng_2_sp)

# vals = eng_2_sp.values()
# print('uno' in vals)  # values


# 9.1 Dictionary as a set of counters  pg. 109

# word = 'brontosaurus'
# d = dict()
# for c in word:
#     if c not in d:
#         d[c] = 1
#     else:
#         d[c] = d[c] + 1

# print(d)


# counts = {'chuck': 1, 'annie': 42, 'jan': 100}
# print(counts.get('jan', 0))
# print(counts.get('tim', 0))


# word = 'brontosaurus'
# d = dict()
# for c in word:
#     d[c] = d.get(c, 0) + 1

# print(d)


# 9.2 Dictionaries and files pg. 110

# fname = input('Enter the file name: ')
# try:
#     fhand = open(fname)
# except:
#     print('File cannot be opened:', fname)
#     exit()

# counts = dict()
# for line in fhand:
#     words = line.split()
#     for word in words:
#         if word not in counts:
#             counts[word] = 1
#         else:
#             counts[word] += 1
# print(counts)


# 9.3 Looping and dictionaries pg. 111

counts = {'chuck': 1, 'annie': 42, 'jan': 100}
# for key in counts:
#     print(key, counts[key])

# for key in counts:
#     if counts[key] > 10:
#         print(key, counts[key])


# lst = counts.keys()
# print(lst)
# print(list(lst))
# print(type(lst))

# lst = list(lst)
# lst.sort()
# print(type(lst))
# print(lst)

# for key in lst:
#     print(key, counts[key])


# 9.4 Advanced text parsing pg. 112


# fname = input('Enter the file name: ')
# try:
#     fhand = open(fname)
# except:
#     print('File cannot be opened:', fname)
#     exit()

# counts = dict()
# for line in fhand:
#     line = line.translate(str.maketrans('', '', string.punctuation))
#     line = line.lower()
#     words = line.split()
#     for word in words:
#         if word not in counts:
#             counts[word] = 1
#         else:
#             counts[word] += 1
# print(counts)
