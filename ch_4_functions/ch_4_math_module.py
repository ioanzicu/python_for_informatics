import math

print(math)

# print(int(3.99999))
# print(int(-2.3))
# print(float(32))
# print(float('3.14159'))

# Calculate signal to noise ratio in Db

signal_power = 9
noise_power = 10
ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)

print('Decibels: ', decibels)


# Find the sinus of radians

radians = 0.7

height = math.sin(radians)
print(f'{radians} radians = {height} sin')


# Convert degrees to radians by dividing 360 and multiply by 2 pi

degrees = 45
radians = degrees / 360.0 * 2 * math.pi
print(f'{degrees} degrees =   {math.sin(radians)} radians')

# Check result

print('Verification: ', math.sqrt(2) / 2.0)
