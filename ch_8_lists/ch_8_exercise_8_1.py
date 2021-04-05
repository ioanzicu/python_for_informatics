# Ex 8.1 pg. 101

def chop(t):
    first = 0
    t.pop(first)

    last = len(t) - 1
    t.pop(last)


letters = ['a', 'b', 'c', 'd', 'e']
print(letters)
chop(letters)
print(letters)
print(chop(letters))


# OR


def chop_2(t):
    first = 0
    del t[first]

    last = len(t) - 1
    del t[last]


letters = ['a', 'b', 'c', 'd', 'e']
print(letters)
chop_2(letters)
print(letters)
print(chop_2(letters))


def middle(t):
    return t[1:len(t) - 1]


letters = ['a', 'b', 'c', 'd', 'e']
print(letters)
print(middle(letters))
print(letters)
