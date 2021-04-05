# Ex 9.1 pg. 108

# Write a program that reads the words in words.txt and stores them
# as keys in a dictionary. It doesn’t matter what the values are. Then you can use
# the in operator as a fast way to check whether a string is in the dictionary.

fhand = open('words.txt')

words = {}
for word in fhand:
    word = word.rstrip()
    words[word] = word

print('text' in words)
print('call' in words)
print('phone' in words)
print('radio' in words)
