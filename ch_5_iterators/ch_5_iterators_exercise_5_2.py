# Ex 5.2 pg. 65


def user_input():
    try:
        user_input = input('Enter a number: ')
        if user_input == 'done':
            return 'done'
        return float(user_input)
    except ValueError as err:
        raise ValueError('Invalid input')


min = None
max = None

while True:
    try:
        user_data = user_input()
    except ValueError as err:
        print(err)
        continue

    if user_data == 'done':
        break

    if min is None or min > user_data:
        min = user_data

    if max is None or max < user_data:
        max = user_data

print('Minimum:', min)
print('Maximum:', max)
