n = 1
while n <= 5:
    print(f"Value is {n:d}")
    n = n + 1
print("List is ready")

# Phase 1
n = 0
while n <= 1000:
    if n % 3 == 0:
        print(str(n))
    n = n + 1

# Phase 2
number_inch = float(input("Input the numbers (inputs a negative value):"))
while number_inch >= 0:
    number_cm = round(number_inch * 2.54, 2)
    print("Converts inches to centimeters:", number_cm)
    number_inch = float(input("Input the numbers (inputs a negative value):"))

# Phase 3
largest = 0
smallest = 0
number = input("Input the numbers:")
if number != "":
    largest = float(number)
    smallest = float(number)
while number != "":
    if float(number) > largest:
        largest = float(number)
    elif float(number) < smallest:
        smallest = float(number)
    number = input("Input the numbers:")
print("The program prints out the largest", largest)
print("The program prints out the smallest", smallest)

# Phase 4
import random
random_number = random.randint(1,10)
guess_number = random.randint(1,10)
guess_number = int(input("Guess the right number from 1 to 10:"))
while random_number != guess_number:
    if guess_number > 10:
        print("wrong number")
    elif random_number < guess_number:
        print("Too high!")
    else:
        print("Too low!")
    guess_number = int(input("Guess the right number from 1 to 10:"))
print("Correct")




