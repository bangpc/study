from utils import number_util, string_util

def menu():
    while True:
        print("------------------------------------------------------")
        print("\nChoose your option:\n1.Capitalize string.\n2.Upper string.\n3.Lower string.\n4.Check odd number.\n5.Check even number.\n6.Find factorial.\n7.Exit.\nChoose 1/2/3/4/5/6/7.")
        user_choice = input("\nEnter your option: ")

        if user_choice == '1':
            string_util.capitalize()

        elif user_choice == '2':
            string_util.upper()

        elif user_choice == '3':
            string_util.lower()

        elif user_choice == '4':
            number_util.is_odd()

        elif user_choice == '5':
            number_util.is_even()

        elif user_choice == '6':
            number_util.factorial()

        elif user_choice == '7':
            print("Exit the program.")
            break

        else:
            print("Invalid option.")

menu()