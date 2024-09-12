import math_utils

def display():
    while True:
        print("\nChoose your option:\n1.Add.\n2.Subtract.\n3.Multiply.\n4.Divide.\n5.Exit.\nChoose 1/2/3/4/5")
        user_choice = input("\nEnter your option: ")

        if user_choice == '1':
            a = input("Enter first number: ")
            b = input("Enter second number: ")
            print(f"The sum of {a} and {b} is: {math_utils.add(a, b)}")

        elif user_choice == '2':
            a = input("Enter first number: ")
            b = input("Enter second number: ")
            print(f"The subtract of {a} and {b} is: {math_utils.subtract(a, b)}")

        elif user_choice == '3':
            a = input("Enter first number: ")
            b = input("Enter second number: ")
            print(f"The multiply of {a} and {b} is: {math_utils.multiply(a, b)}")

        elif user_choice == '4':
            a = input("Enter first number: ")
            b = input("Enter second number: ")
            print(f"The divide of {a} and {b} is: {math_utils.divide(a, b)}")

        elif user_choice == '5':
            print("Exit the program.")
            break

        else:
            print("Invalid option.")
