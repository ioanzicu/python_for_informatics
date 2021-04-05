fruit = 'banana'
letter = fruit[1]

length = len(fruit)
last = fruit[length-1]

# print(letter)
# print(length)
# print(last)
# print(fruit[-1])


# 6.3 pg. 68

# index = 0
# while index < len(fruit):
#     letter = fruit[index]
#     print(letter)
#     index = index+1


# print('-------')


# Exercise 6.1 pg.68

# index = len(fruit) - 1
# while index >= 0:
#     letter = fruit[index]
#     print(letter)
#     index = index-1


# for char in fruit:
#     print(char)


# 6.4 String slices

# s = 'Monty Python'
# print(s[0:5])
# print(s[6:12])


# print(fruit[:3])
# print(fruit[3:])

# print(fruit[3:3])

# fruit_2 = fruit[:]
# print(fruit_2)


# 6.5 Strings are immutable pg. 69

greeting = 'Hello, world!'

new_greeting = 'J' + greeting[1:]
# print(new_greeting)


# 6.6 Looping and counting pg. 70

# word = 'banana'
# count = 0
# for letter in word:
#     if letter == 'a':
#         count = count + 1

# print(count)


# Exercise 6.3

# def count_char(word: str, char: str):
#     count = 0
#     for letter in word:
#         if letter == char:
#             count = count + 1

#     print(count)


# count_char('banana', 'a')


# 6.7 The in operator pg. 70

# if 'a' in 'banana':
#     print('OMG!!!')


# 6.8 String comparision pg. 70
# word = 'banana'
# if word == 'banana':
#     print('All right, bananas.')


# word = 'Banana'
# if word < 'banana':
#     print('Your word, ' + word + ', comes before banana.')
# elif word > 'banana':
#     print('Your word, ' + word + ', comes after banana.')
# else:
#     print('All right, banannas.')


# 6.9 string methods pg. 71
stuff = 'Hello world'
# print(type(stuff))
# print(dir(stuff))
# print(help(str.capitalize))


# new_stuff = stuff.upper()
# print(new_stuff)


# index = stuff.find('wo')
# print(index)


# line = '    Her we go again!!!    '
# print(line.strip())


line = 'Please have a nice day and focus on important for you things ;)'
# print(line.startswith('Please'))

# print(line.startswith('p'))

# print(line.lower())
# print(line.lower().startswith('p'))


# Exercise 6.4 pg. 73

# word = 'banana'
# print(word.count('a'))


# 6.10 Parsing strings pg. 73

# data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# atpos = data.find('@')
# print(atpos)

# sppos = data.find(' ', atpos)
# print(sppos)

# host = data[atpos+1:sppos]
# print(host)


# 6.11 Format operator pg. 74

# camels = 42
# print('i have spotted %d camels.' % camels)


# print('In %d years I have spotted %g %s.' % (3, 0.1, 'camels'))
# print('%d %d %d' % (1, 22, 333))
