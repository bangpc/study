from utils import file_util

def menu():
    while True:
        print("------------------------------------------------------")
        print("\nChoose your option:\n1.List file.\n2.Delete file.\n3.Modify file.\n4.Exit.\nChoose 1/2/3/4.")
        user_choice = input("\nEnter your option: ")

        if user_choice == '1':
            file_util.list_file()

        elif user_choice == '2':
            file_util.delete_file()
            
        elif user_choice == '3':
            file_util.modify_file()

        elif user_choice == '4':
            print("Exit the program.")
            break

        else:
            print("Invalid option.")

menu()