# Ex 10.1 pg 127

# Revise a previous program as follows: Read and parse the “From”
# lines and pull out the addresses from the line. Count the number of messages from
# each person using a dictionary.

# After all the data has been read, print the person with the most commits by creating
# a list of (count, email) tuples from the dictionary. Then sort the list in reverse order
# and print out the person who has the most commits.

# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
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


# Decorate - dict to list of tuples
lst = list()
for email, count in email_senders.items():
    lst.append((count, email))

# Sort by count (first value)
lst.sort(reverse=True)

# Undecorate - extract the data that we need
count, email = lst[0]
print(email, count)
