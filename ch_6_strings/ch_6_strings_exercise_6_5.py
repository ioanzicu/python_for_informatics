# 6.5 pg. 77

string = 'X-DSPAM-Confidence: 0.8475'

sppos = string.find(' ')
print(sppos)

str_numbers = string[sppos+1:]
print(str_numbers)
print(type(str_numbers))

float_numbers = float(str_numbers)
print(float_numbers)
print(type(float_numbers))
