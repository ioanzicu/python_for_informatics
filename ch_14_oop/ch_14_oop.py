# 14.3 Using objects pg. 174 (Python for Everybody)

# stuff = list()
# stuff.append('python')
# stuff.append('chuck')
# stuff.sort()
# print(stuff[0])
# print(stuff.__getitem__(0))
# print(list.__getitem__(stuff, 0))

# print(dir(stuff))


# 14.6 Our first object pg 177

# class PartyAnimal:
#     x = 0

#     def party(self):
#         self.x = self.x + 1
#         print('So far', self.x)


# an = PartyAnimal()
# ab = PartyAnimal()
# an.party()
# an.party()
# an.party()
# PartyAnimal.party(an)
# PartyAnimal.party(ab)
# PartyAnimal.party(ab)


# 14.7 Classes as types pg 180

# class PartyAnimal:
#     x = 0

#     def party(self):
#         self.x = self.x + 1
#         print('So far', self.x)


# an = PartyAnimal()
# print('Type', type(an))
# print('Dir', dir(an))
# print('Type', type(an.x))
# print('Type', type(an.party))


# 14.8 Object lifecycle pg 181


# class PartyAnimal:
#     x = 0

#     def __init__(self):
#         print('I am constructed')

#     def party(self):
#         self.x = self.x + 1
#         print('So far', self.x)

#     def __del__(self):
#         print('I am destructed', self.x)


# an = PartyAnimal()
# an.party()
# an.party()
# an = 42  # old object is destroyd - __del__ method is called
# print('an contains', an)


# 14.9 Multiple instances pg 182


# class PartyAnimal:
#     x = 0
#     name = ''

#     def __init__(self, nam):
#         self.name = nam
#         print(self.name, 'constructed')

#     def party(self):
#         self.x = self.x + 1
#         print(self.name, 'party count', self.x)


# s = PartyAnimal('Sally')
# j = PartyAnimal('Jim')

# s.party()
# j.party()
# s.party()


# 14.10 Inheritance pg 183


from party import PartyAnimal


class CricketFan(PartyAnimal):
    points = 0

    def six(self):
        self.points = self.points + 6
        self.party()
        print(self.name, 'points', self.points)


s = PartyAnimal('Sally')
s.party()
j = CricketFan('Jim')
j.party()
j.six()
print(dir(j))
