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
    n = n+1

# Phase 2
number_inch = float(input("Input the numbers (inputs a negative value):"))
while number_inch >= 0:
    number_cm = round(number_inch * 2.54,2)
    print("Converts inches to centimeters:", number_cm)
    number_inch = float(input("Input the numbers (inputs a negative value):"))

# Phase 3
largest = 0
number = float(input("Input the numbers:"))


