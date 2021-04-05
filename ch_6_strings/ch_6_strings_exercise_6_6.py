# 6.6 pg. 77

string = 'Hello, World! Lets. get rid of some bad punctuation!'

string_1 = string.replace(',', '')
print(string_1)

string_2 = string.replace('.', ',')
print(string_2)


some_string = 'Hello World! Lets remove the exclamation mark!,.'

some_string_1 = some_string.strip('.!,')
print(some_string_1)
