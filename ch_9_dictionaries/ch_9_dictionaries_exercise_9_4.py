# Ex. 9.4 pg. 116

# Add code to the above program to figure out who has the most messages
# in the file.
# After all the data has been read and the dictionary has been created, look through
# the dictionary using a maximum loop (see Section 5.7.2) to find who has the most
# messages and print how many messages the person has.

# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
# Enter a file name: mbox.txt
# zqian@umich.edu 195

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


max_count = None
max_count_sender = None

for key in email_senders.keys():
    if max_count is None or max_count < email_senders[key]:
        max_count = email_senders[key]
        max_count_sender = key


print(max_count_sender, max_count)
