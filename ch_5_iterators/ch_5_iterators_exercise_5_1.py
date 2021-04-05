# Ex 5.1 pg. 65


def user_input():
    try:
        user_input = input('Enter a number: ')
        if user_input == 'done':
            return user_input
        return float(user_input)
    except ValueError as err:
        raise ValueError('Invalid input')


total = 0.0
average = 0.0
count = 0


while True:
    try:
        user_data = user_input()
    except ValueError as err:
        print(err)
        continue

    if user_data == 'done':
        break

    total = total + user_data
    count = count + 1

average = total / count

print('Total:', total)
print('Count:', count)
print('Average:', average)
