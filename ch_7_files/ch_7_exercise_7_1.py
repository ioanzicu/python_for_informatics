# 7.1 pg. 88

fname = input('Enter a file name: ')
try:
    fhandle = open(fname)
except:
    print(f'File {fname} not found')
    exit()

for line in fhandle:
    print(line.upper())
