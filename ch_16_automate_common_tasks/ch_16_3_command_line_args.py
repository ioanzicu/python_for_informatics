import sys

try:
    name = sys.argv[1]
    fhandle = open(name, 'r')
    text = fhandle.read()
    print(name, 'is', len(text), 'bytes')
except:
    print('Try to run the script passing the .txt file name as second argument.')
