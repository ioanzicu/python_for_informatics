# Ex 16.1 pg 212

# In a large collection of MP3 files there may be more than one copy
# of the same song, stored in different directories or with different file names. The
# goal of this exercise is to search for these duplicates.

# 1. Write a program that walks a directory and all of its subdirectories for all
# files with a given suffix (like .mp3) and lists pairs of files with that are the
# same size. Hint: Use a dictionary where the key of the dictionary is the size
# of the file from os.path.getsize and the value in the dictionary is the path
# name concatenated with the file name. As you encounter each file, check
# to see if you already have a file that has the same size as the current file. If
# so, you have a duplicate size file, so print out the file size and the two file
# names (one from the hash and the other file you are looking at).

# 2. Adapt the previous program to look for files that have duplicate content
# using a hashing or checksum algorithm. For example, MD5 (Message-
# Digest algorithm 5) takes an arbitrarily-long “message” and returns a 128-
# bit “checksum”. The probability is very small that two files with different
# contents will return the same checksum.
# You can read about MD5 at wikipedia.org/wiki/Md5. The following
# code snippet opens a file, reads it, and computes its checksum.

import os
import hashlib
from os.path import join

original_files = dict()
hash_files = dict()

for (dirname, dirs, files) in os.walk('.'):
    # print(dirname, dirs, files)
    for filename in files:
        if filename.endswith('.mp3'):
            thefile = os.path.join(dirname, filename)
            filesize = os.path.getsize(thefile)

            fhand = open(thefile, 'rb',)
            data = fhand.read()
            fhand.close()
            checksum = hashlib.md5(data).hexdigest()
            # print('Checksum', checksum)

            if filesize not in original_files:
                original_files[filesize] = thefile
            else:
                print('COPY', filename)

            if checksum not in hash_files:
                hash_files[checksum] = thefile
            # else:
            #     print('COPY', filename)


print('\nSIZE:')

for size, file_path in original_files.items():
    print('Path:', file_path, size, 'bytes')

print('\nCHECKSUM:')

for checksum, file_path in hash_files.items():
    print('Checksum:', file_path, checksum, 'bytes')
