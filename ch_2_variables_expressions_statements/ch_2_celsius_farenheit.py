# Ex. 2.5 pg. 30

# Write a program which prompts the user for a Celsius temperature,
# convert the temperature to Fahrenheit, and print out the converted temperature.

def get_input(message: str) -> float:
    '''Prompt user for input and handle non-float ValueError conversion.'''

    while True:
        try:
            degrees = float(input(message))
            return degrees
        except ValueError as err:
            print('Enter a integer or float value!!!')


def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * (9.0/5.0)) + 32.0


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32.0) * (5.0/9.0)


def convert_celsius_to_fahrenheit():
    celsius_degrees = get_input('Enter celsius degrees: ')
    fahrenheit_degrees = celsius_to_fahrenheit(celsius_degrees)
    print(f'{celsius_degrees} Celsius = {fahrenheit_degrees:.2f} Fahrenheit')


def convert_fahrenheit_to_celsius():
    fahrenheit_degrees = get_input('Enter Fahrenheitdegrees: ')
    celsius_degrees = fahrenheit_to_celsius(fahrenheit_degrees)
    print(f'{fahrenheit_degrees} Fahrenheit = {celsius_degrees:.2f} Celsius')


def prompt_input():

    print('''Select option:
    1. Convert Celsius to Fahrenheit Degrees
    2. Convert Fahrenheitto Celsius Degrees
    ''')
    return int(get_input('Select option: '))


def number_to_option(argument: int):
    switcher = {
        1: convert_celsius_to_fahrenheit,
        2: convert_fahrenheit_to_celsius
    }

    # Get the function from switcher dictionary
    func = switcher.get(argument, 0)

    # Handle invalid option case
    if func == 0:
        print(f'Invalid option: {argument}. Try again!!!\n')
        return 0

    # Execute the function
    return func()


user_option = prompt_input()
while number_to_option(user_option) == 0:
    user_option = prompt_input()

print('\nThe program has successfully completed!!!\nHave a nice day ;)\n')
