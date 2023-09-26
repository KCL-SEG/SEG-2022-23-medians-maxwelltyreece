"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        numbers.sort()
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

if len(numbers) == 1:
    print(numbers[0])
elif len(numbers) % 2 == 0:
    print( (numbers[int( (len(numbers)/2)-1 )] + numbers[int(len(numbers)/2)]) / 2)

else:
    print(numbers[int( (len(numbers)-1) / 2 )])