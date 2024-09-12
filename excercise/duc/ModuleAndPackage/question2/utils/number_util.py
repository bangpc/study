import math

def is_odd():
    x = input("Enter number: ")
    if int(x) % 2 != 0:
        print(f"{x} is odd number")
    else:
        print(f"{x} is not odd number")

def is_even():
    x = input("Enter number: ")
    if int(x) % 2 == 0:
        print(f"{x} is even number")
    else:
        print(f"{x} is not even number")

def factorial():
    x = input("Enter number: ")
    print(f"The factorial of {x} is: {math.factorial(int(x))}")
