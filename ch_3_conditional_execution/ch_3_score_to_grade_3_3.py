# Ex. 3.3 pg. 41

# Write a program to prompt for a score between 0.0 and 1.0. If the
# score is out of range, print an error message. If the score is between 0.0 and 1.0,
# print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# Enter score: 0.95
# A
# Enter score: perfect
# Bad score
# Enter score: 10.0
# Bad score
# Enter score: 0.75
# C
# Enter score: 0.5
# F
# Run the program repeatedly as shown above to test the various different values for
# input.

def user_input(banner: str, message: str, error_message: str):
    print(banner)

    while True:
        try:
            value = float(input(message))
            if value < 0.0 or value > 1.0:
                raise ValueError

            return value
        except ValueError as err:
            print(error_message)


def computegrade(score: float) -> str:

    grade = ''
    if user_input >= 0.9 and user_input <= 1.0:
        grade = 'A'
    elif user_input >= 0.8 and user_input < 0.9:
        grade = 'B'
    elif user_input >= 0.7 and user_input < 0.8:
        grade = 'C'
    elif user_input >= 0.6 and user_input < 0.7:
        grade = 'D'
    elif user_input >= 0 and user_input < 0.6:
        grade = 'F'
    else:
        grade = error_message

    return grade


banner = '''
    Score     Grade
    >= 0.9      A
    >= 0.8      B
    >= 0.7      C
    >= 0.6      D
    < 0.6       F
    '''
error_message = 'Bad Score!!!'
user_input = user_input(banner, 'Enter score: ', error_message)

grade = computegrade(user_input)
print(grade)
