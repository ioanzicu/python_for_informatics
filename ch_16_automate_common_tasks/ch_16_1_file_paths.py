import os

cwd = os.getcwd()
print('CWD:', cwd)

p = os.path.abspath('memo.txt')
print(p)
print(os.path.exists('memo.txt'))
print(os.path.isdir('memo.txt'))
print(os.path.isdir('ch_14_sqlite'))
print(os.path.isfile('f.txt'))

ldir = os.listdir(cwd)
print(ldir)
