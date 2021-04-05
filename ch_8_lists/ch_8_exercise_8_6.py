# Ex. 8.6 pg. 106

# Rewrite the program that prompts the user for a list of numbers and
# prints out the maximum and minimum of the numbers at the end when the user
# enters “done”. Write the program to store the numbers the user enters in a list
# and use the max() and min() functions to compute the maximum and minimum
# numbers after the loop completes.
# Enter a number: 6
# Enter a number: 2
# Enter a number: 9
# Enter a number: 3
# Enter a number: 5
# Enter a number: done
# Maximum: 9.0
# Minimum: 2.0


def user_input():
    try:
        user_input = input('Enter a number: ')
        if user_input == 'done':
            return 'done'
        return float(user_input)
    except ValueError as err:
        raise ValueError('Invalid input')


numbers = []

while True:
    try:
        user_data = user_input()
    except ValueError as err:
        print(err)
        continue

    if user_data == 'done':
        break

    numbers.append(user_data)

print('Minimum:', min(numbers))
print('Maximum:', max(numbers))
