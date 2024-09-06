import pandas as pd

def column_string_to_column_index(string):
    num = 0
    for i, char in enumerate(reversed(string)):            
        num += (ord(char) - ord('A') + 1) * (26 ** i)
    return num - 1

class excel_file():
    def __init__(self, name) -> None:
        self.name = name

    def print_out_data(self):
        data = pd.read_excel(f'{self.name}')
        print(data)

    def insert_data(self):
        content = input("Enter the content: ")
        row = input("Enter the row of cell: ")
        column = input("Enter the column of cell: ")
        row_index = int(row) - 1
        column_index = column_string_to_column_index(column)

        data = pd.read_excel(f'{self.name}')

        if column_index >= len(data.columns):
            for _ in range(len(data.columns), column_index + 1):
                data[f'NewColumn{_ + 1}'] = pd.NA

        if row_index >= len(data):
            data = data.reindex(range(row_index + 1))
        
        data.iat[row_index, column_index] = f'{content}'
        data.to_excel(self.name, index=False, header=True)
        print(f"The data at cell [{row}, {column}] is {content}")
        
def main():
    filename = input("Enter the filename (It must be end with .xlsx): ")
    file = excel_file('Question_5.xlsx')

    while True:
        print("\nChoose your option:\n1.Print out current data\n2.Insert data into a specific cell\n3.Exit\nChoose 1/2/3")
        user_choice = input("\nEnter your option: ")

        if user_choice == '1':
            file.print_out_data()

        elif user_choice == '2':
            file.insert_data()

        elif user_choice == '3':
            print("Exit the program.")
            break

        else:
            print("Invalid option.")

main()