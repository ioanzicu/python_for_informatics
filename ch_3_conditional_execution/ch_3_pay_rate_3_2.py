# Ex. 3.2 pg. 40

# Rewrite your pay program using try and except so that your program
# handles non-numeric input gracefully by printing a message and exiting the
# program. The following shows two executions of the program:
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input
# Enter Hours: forty
# Error, please enter numeric input

def user_input(message: str) -> float:
    while True:
        try:
            return int(input(message))
        except ValueError as err:
            print('Invalid value type, just int or float accepted.')


hours = user_input('Enter Hours: ')
rate = user_input('Enter Rate: ')


def computepay(hours: float, rate: float):
    extra_hours = 0.0
    if hours > 40.0:
        extra_hours = hours - 40.0
        normal_payment = 40.0 * rate
        extra_payment = extra_hours * (rate * 1.5)
        total_payment = normal_payment + extra_payment
        print(f'Pay: {total_payment:.1f}')
    else:
        normal_payment = hours * rate
        print(f'Pay: {normal_payment:.1f}')


computepay(hours, rate)
