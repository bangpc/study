import os
from .advances import advance_util

folder = "D:/SoruceCode/Python/study/excercise/duc/ModuleAndPackage/question3/files"

def list_file():
    print("List of file:")
    for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            if os.path.isfile(file_path):
                print(filename)

def delete_file():
    list_file()
    filename = input("Enter filename to delete: ")
    file_path = os.path.join(folder, filename)
    if os.path.exists(f"{file_path}"):
        os.remove(f"{file_path}")
        print(f'{filename} is deleted.')
    else:
        print(f'{filename} does not exist.')

def modify_file():
    print("Choose your option to modify file:\nA.Remove line.\nB.Add content.\nC.Exit modify file\nChoose A/B/C")
    choose = input("\nEnter your option: ")
    while True:
        if choose == 'A':
            advance_util.remove_line()
            break
        elif choose == 'B':
            advance_util.add_content()
            break
        elif choose == 'C':
            print("Exit modify file!")
            break
        else:
            print("Invalid option!")
            break

