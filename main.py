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

# Phase 5
username = "XuanDang"
password = "Sunny1109"
count = 0
username = input("Enter the username:")
password = input("Enter the password:")
while (username != "XuanDang" or password != "Sunny1109") and count < 4:
    print("Access denied. Try again.")
    username = input("Enter the username:")
    password = input("Enter the password:")
    count = count + 1
if username == "XuanDang" and password == "Sunny1109":
        print("Welcome")
else:
        print("Access denied")

# Phase 6
import math
import random
number = int(input("Random points to generate:"))
inside_circle = 0
count = 0
while number > count:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x*x + y*y < 1:
        inside_circle = inside_circle + 1
    count = count + 1
a = 4 * inside_circle / number
print("The approximate value of pi: ", a)
