# Dictionary UPDATE

# V - 1

# d1 = {'foo': 1}
# d2 = {'bar': 2}
# print(d1)
# print(d2)

# d1.update(d2)
# print(d1)
# print(d2)

# d1['bar'] = 33
# print(d1)
# print(d2)


# V - 2

# d1 = {'foo': 1}
# d2 = {'bar': 2}
# d3 = {**d1, **d2}
# print(d1)
# print(d2)
# print(d3)
# d3['foo'] = 3
# print(d3)


# V - 3 - it modifies the original dictionary if modifiy the original

# from collections import ChainMap

# d1 = {'foo': 1}
# d2 = {'bar': 2}

# print(d1)
# print(d2)

# merged = ChainMap(d2, d1)
# merged['bar'] = 999

# print(merged)
# print(d1)
# print(d2)


# V - 4 Merge Operator "|"

# d1 = {'foo': 1, 'bar': 2}
# d2 = {'baz': 3}
# d3 = {'lol': 4}
# print(d1)
# print(d2)
# print(d3)

# dd1 = d1 | d2 | d3
# print(dd1)

# dd2 = d2 | d1 | d3
# print(dd2)
# dd2['foo'] = 333333
# print(dd2)


# V - 5 Update Operator "|="

# d1 = {'foo': 1, 'bar': 2}
# print(d1)

# d1 |= [('baz', 3)]
# print(d1)


# l = list[str]()
# print(l)

# print(list is list[str])
# print(list == list[str])
# print(list[str] == list[str])

# L----------------O-------------L

# values = [1, 2, 1, 3]
# nums = set(values)


# def check(num):
#     if num in nums:
#         return True
#     else:
#         return False


# for i in filter(check, values):
#     print(i)


# try:
#     x = 1/0
#     f = open('sdads.txt')
# except ZeroDivisionError as e:
#     print('zero')
# except FileNotFoundError as e:
#     print('no file')
# except:
#     print('all done')


# print((1, 2, 4, 3)[1:3])

# f = open('f.txt')
# print(f.readline())
# print(f.readline())
# print(f.readline())


# def m_two(n): return n*2
# def m_tree(n): return n*3


# x = 2
# x = m_two(x)
# x = m_tree(x)
# x = m_two(x)
# print(x)


# name = 'thunder storm'
# name[8] = 'X'
# print(name)


# print({'george': 40, 'peter': 45}['susan'])


# n1 = 1
# n2 = '2'
# n3 = 3

# sum = 0

# for i in (n1, n2, n3):
#     if isinstance(i, int):
#         sum += i
# print(sum)


# def foo(l1):
#     l1[0] = 1

# tl = [0]
# foo(tl)
# print(tl)


# foo = 0


# def bar():
#     global foo
#     foo += 1
#     print(foo)


# def baz():
#     print(foo)


# def taz():
#     foo = 10
#     print(foo)


# bar()
# print(foo)
# taz()
# baz()


# def test():
#     pass


# print(type(test))
# print(type(test()))


# -----------------------

# counter = 1


# def do_stuff():
#     global counter
#     for i in (1, 2, 3, 4,):
#         counter += 1


# do_stuff()
# print(counter)


# -----------------------


# try:
#     print('ssksk')
# except:
#     print('ssss')
# finally:
#     print('LOL')


# -----------------------


# def foo():
#     return total + 1


# total = 0
# print(foo())


# -----------------------


# l = [1, 2, 3]


# def change_list(l):
#     l.append([1, 2, 3])
#     return l


# k = change_list(l)
# print(k)
# print(len(k))


# -----------------------

# class First(object):
#     x = 1


# class Second1(First):
#     pass


# class Second2(First):
#     pass


# print(First.x, Second1.x, Second2.x)
# Second1.x = 2
# print(First.x, Second1.x, Second2.x)
# First.x = 3
# print(First.x, Second1.x, Second2.x)

# -----------------------


# def foo(fun, val):
#     print(fun(val))


# foo(max, [1, 2, 3])
# foo(min, [1, 2, 3])


# -----------------------

# fruits = ['apple', 'orange', 'watermelon']
# months = ['Jan',
#           'Feb']

# print('fruits: %s, months %s' % (fruits, months))


# -----------------------

# t_tuple = (1, 2, 3, 4)
# t_tuple.append((5, 6, 7))
# print(len(t_tuple))


# -----------------------


# d = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5}
# new_data = {'1': 10, '3': 30}

# d.update(new_data)

# print(d)
# x = sum(d.values())

# print(x)


# -----------------------


# -----------------------


# def test_func():
#     try:
#         print(1)
#     finally:
#         print(2)


# test_func()


# -----------------------


# names = ['Cersei', 'Arya', 'John', 'Mao']
# print(names[-1][-1])


# -----------------------


# my_d = {'user', 'bill', 'password', 'hillary'}
# print(my_d['password'])


# -----------------------


# names = ['Cersei', 'Arya', 'John', 'Mao']
# loc = names.index('Edward')
# print(loc)


# -----------------------


# d = {'george': 40, 'peter': 45}
# print(list(d.keys()))


# -----------------------


# import sys
# print(sys.path, '\n\n')
# p = sys.path.append('/root/mods')
# print(p, '\n\n')

# print(sys.path.append('/root/mods'))


# -----------------------


# a = [1, 2, 3, None, (), []]
# print(len(a))
# a[len(a):] = [3, ]
# print(a)
# print(len(a))


# -----------------------


# list = ['f', 'g', 'h', 'i', 'j']
# print(list[12:])


# -----------------------


# t = (1, 2, 4, 3, 8, 9)
# print([t[i] for i in range(0, len(t), 2)])


# -----------------------


# def main():
#     try:
#         fh = open('notfound.txt')
#         for line in fh:
#             print(line.strip())
#     except IOError as e:
#         print('Unable to open file:', e)


# main()


# -----------------------


# lst = ['spam', 'and', 'eggs']
# lst[2] = 'toast'
# print('_'.join(lst))


# -----------------------


# l = [1, 2, 3]


# def change_list(l):
#     print(l.append(5))
#     return l


# k = change_list(l)
# print(l)
# print(k)


# -----------------------


# def test_func():
#     try:
#         return 1
#     finally:
#         return 2


# k = test_func()
# print(k)


# -----------------------


# num_d = {}
# num_d[(1, 2, 4)] = 8
# num_d[(4, 2, 1)] = 10
# num_d[(1, 2)] = 12

# sum = 0

# for k in num_d:
#     sum += num_d[k]

# print(len(num_d) + sum)


# -----------------------


# a = 1
# b = 2
# a, b = b, a
# print('%d %d' % (a, b))


# -----------------------


# from __future__ import division


# def div1(x, y):
#     print('%s/%s=%s' % (x, y, x/y))


# def div2(x, y):
#     print('%s//%s=%s' % (x, y, x//y))


# div1(5, 2)
# div1(5., 2)
# div2(5, 2)
# div2(5, 2.)


# -----------------------


# name = 'Jon'
# s = name.rjust(4, 'A')
# print(s)


# -----------------------


# print(12 ** 3)
# print(pow(12, 3))

# print('12 ** 3')
# print('pow(12, 3)')


# -----------------------


# name = 'snow storm'
# print('%srm' % name[6:8])


# -----------------------


# names = ['George', 'John', 'Liam', 'Waiter', 'Nico']
# print('\n'.join(names))


# -----------------------


# t = (1, 2,)
# x = 2*t
# t = (t, x)
# print(t)


# -----------------------


# counter = {}


# def one_more(country):
#     if country in counter:
#         counter[country] += 1
#     else:
#         counter[country] = -1


# one_more('Honduras')
# one_more('India')
# one_more('honduras')

# print(len(counter))


# -----------------------


# dict = {}
# dict[1] = 1
# dict['2'] = 2
# dict[1] += 1

# sum = 0
# for k in dict:
#     print(k)
#     sum += dict[k]

# print(sum)


# -----------------------


# test = (3, 4, 5, {}, [],)
# print(type(test))


# -----------------------


# t1 = (1, 2, 4, 3)
# t2 = (1, 2, 3, 4)
# print(t1 < t2)


# -----------------------


# print(isinstance(2, int))


# -----------------------


# t1 = (1, 2, 4, 3)
# print(t1[1:-1])


# -----------------------


# values = [2, 3, 2, 4]


# def transformation(num):
#     return num ** 2


# for i in map(transformation, values):
#     print(i)


# -----------------------


# n = '\ntest1\ntest2\n'.strip()
# print(n)


# -----------------------


# fh = open('f.txt')
# print(fh.read(2))


# -----------------------


# f = None
# for i in range(5):
#     with open('f.txt', 'w') as f:
#         if i > 2:
#             break
# print(f.closed)


# -----------------------


# print(r'\nHello')


# -----------------------


# test_dict = {1: '1', 2: '2', 3: '3'}
# test_dict = {}
# print(len(test_dict))


# -----------------------


# for num in range(2):
#     print(num)

# for num in range(4, 6):
#     print(num)

# print(num)


# -----------------------
