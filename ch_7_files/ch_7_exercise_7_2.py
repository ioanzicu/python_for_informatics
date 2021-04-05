# 7.2 pg. 89

fname = input('Enter the file name: ')
try:
    fhandle = open(fname)
except:
    print(f'File {fname} not found')


total_spam_confidence = 0.0
count = 0
for line in fhandle:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue

    count = count + 1

    start = line.find(': ')
    end = len(line)

    spam_confidence = float(line[start+1:end])
    total_spam_confidence = total_spam_confidence + spam_confidence


avg_spam_confidence = total_spam_confidence / float(count)
print('Average spam confidence:', avg_spam_confidence)
