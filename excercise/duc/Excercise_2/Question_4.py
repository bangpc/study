import os
class TextManagement():
    def __init__(self, folder) -> None:
        self.folder = folder

    def print_all_files(self):
        for filename in os.listdir(self.folder):
            file_path = os.path.join(self.folder, filename)
            if os.path.isfile(file_path):
                print(filename)

    def print_content(self, filename):
        file_path = os.path.join(self.folder, filename)
        if os.path.exists(f"{file_path}"):
            f = open(f"{file_path}", "r")
            print(f'Content in {filename}:')
            print(f.read())
        else:
            print(f'{filename} does not exist.')

    def replace_content(self, filename, new_content):
        file_path = os.path.join(self.folder, filename)
        if os.path.exists(f"{file_path}"):
            f = open(f"{file_path}", "w")
            f.write(f"{new_content}")
            f.close()
            print(f'Content in {filename} is replaced.')
        else:
            print(f'{filename} does not exist.')

    def add_new_file_with_content(self, filename, new_content):
        file_path = os.path.join(self.folder, filename)
        if os.path.exists(f"{file_path}"):
            print(f'{filename} is existed.')
        else:
            f = open(f"{file_path}", "w")
            f.write(f"{new_content}")
            f.close()
            print(f'{filename} is added.')

    def delete_selected_file(self, filename):
        file_path = os.path.join(self.folder, filename)
        if os.path.exists(f"{file_path}"):
            os.remove(f"{file_path}")
            print(f'{filename} is deleted.')
        else:
            print(f'{filename} does not exist.')

def main():
    folder = input("Enter the path of the folder: ")
    file = TextManagement(folder)

    while True:
        print("\nChoose your option:\n1.Print all files in the folder\n2.Print content in a selected file in the folder\n3.Replace the content of selected file\n4.Add a new file to folder with content from user input\n5.Delete selected file\n6.Exit\nChoose 1/2/3/4/5/6")
        user_choice = input("\nEnter your option: ")

        if user_choice == '1':
            file.print_all_files()

        elif user_choice == '2':
            filename = input("Enter file name: ")
            file.print_content(filename)

        elif user_choice == '3':
            filename = input("Enter file name: ")
            new_content = input("Enter new content: ")
            file.replace_content(filename, new_content)
        
        elif user_choice == '4':
            filename = input("Enter file name: ")
            new_content = input("Enter new content: ")
            file.add_new_file_with_content(filename, new_content)
        
        elif user_choice == '5':
            filename = input("Enter file name: ")
            file.delete_selected_file(filename)

        elif user_choice == '6':
            print("Exit the program.")
            break

        else:
            print("Invalid option.")

main()

        
