# Ex. 9.3 pg. 116

# Write a program to read through a mail log, build a histogram using
# a dictionary to count how many messages have come from each email address,
# and print the dictionary.
# Enter file name: mbox-short.txt
# {'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
# 'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
# 'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
# 'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
# 'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
# 'ray@media.berkeley.edu': 1}

fname = input('Enter a file name: ')

try:
    fhand = open(fname)
except:
    print('Cannot find file:', fname)
    exit()

email_senders = {}
for line in fhand:
    words = line.split()
    if len(words) > 2 and words[0] == 'From':
        sender = words[1]
        email_senders[sender] = email_senders.get(sender, 0) + 1

print(email_senders)
