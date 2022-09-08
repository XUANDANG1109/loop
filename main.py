# NAME: XUAN DANG

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

# Phase 2 solution
prompt = "Give me inches"
inch = float(input(prompt))
while inch >= 0:
    print(f"It is in centimeters: {inch*2.54:.1f}")
    inch = float(input(prompt))

# Phase 3 solution
prompt = "Give a number"
s = input(prompt)
smallest = int(s)
largest = smallest
while s!= "":
    n = int(s)
    if n<smallest:
        smallest = n
    if n > largest:
        largest = n
    s = input(prompt)
else:
    print(f"The smallest number given was: {smallest}, amd the largest was {largest}")

# Phase 4
import random
the_number = random.randint(1,10)
prompt = "Try to guess the number"
guess = int(input(prompt))
while guess != the_number:
    if guess > the_number:
        print("Too high")
    else:
        print("Too low")
    guess = int(input(prompt))
else:
    print("Correct")

# Phase 5
username = "python"
password = "rules"
n = 5
while n > 0:
    u = input("Give the username:")
    p = input("Give the passport:")
    if u == username and p == password:
        print("Welcome")
        break
    n = n -1
else:
    print("Access denied")

# Phase 6
import math
import random
N = int(input("How many random points to generate?"))
n = 0
i = 0
while i < N :
    x = random.uniform(-1.,1.)
    y = random.uniform(-1.,1.)

    if x**2 + y**2 <1.:
        n = n + 1
    i = i + 1
pi = 4*n/N
print(f"Pi is {pi}, error {math.pi - pi}")
