import os

folder = "D:/SoruceCode/Python/study/excercise/duc/ModuleAndPackage/question3/files"

def print_content(filename):
        file_path = os.path.join(folder, filename)
        if os.path.exists(f"{file_path}"):
            f = open(f"{file_path}", "r")
            print(f'Content in {filename}:')
            print(f.read())
        else:
            print(f'{filename} does not exist.')

def remove_line():
    filename = input("Enter filename to remove line: ")
    file_path = os.path.join(folder, filename)
    print_content(filename)
    line_to_delete = int(input("Enter number of line to delete: "))
    with open(file_path, "r") as file:
        lines = file.readlines()

    if 0 <= line_to_delete< len(lines):
        del lines[line_to_delete - 1]

    with open(file_path, 'w') as file:
        file.writelines(lines)

    print(f"Line {line_to_delete} has been deleted.")

def add_content():
    filename = input("Enter filename to add content: ")
    file_path = os.path.join(folder, filename)
    content = input("Enter new content: ")
    f = open(f"{file_path}", "a")
    f.write(f"{content}")
    f.close()
    print(f"New content ({content}) added to file {filename}.")
