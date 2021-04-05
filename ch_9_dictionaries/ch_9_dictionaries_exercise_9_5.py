# Ex. 9.5 pg. 116

# This program records the domain name (instead of the address)
# where the message was sent from instead of who the mail came from (i.e., the
# whole email address). At the end of the program, print out the contents of your
# dictionary.

# python schoolcount.py
# Enter a file name: mbox-short.txt
# {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
# 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}


fname = input('Enter a file name: ')

try:
    fhand = open(fname)
except:
    print('Cannot find file:', fname)
    exit()

domain_email_senders = {}
for line in fhand:
    words = line.split()
    if len(words) > 2 and words[0] == 'From':
        sender = words[1]
        domain = sender.split('@')[1]
        domain_email_senders[domain] = domain_email_senders.get(domain, 0) + 1


print(domain_email_senders)
