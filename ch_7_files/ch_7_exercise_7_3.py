# 7.3 pg. 89

fname = input('Enter a file name: ')

if fname == 'na na boo boo':
    print('NA NA BOO BOO TO YOU - You have been punk\'d!')
    exit()

try:
    fhandle = open(fname)
except:
    print(f'File {fname} not found')
    exit()

count = 0
for line in fhandle:
    if line.startswith('Subject:'):
        count = count + 1

print('There were', count, 'subject lines in', fname)
