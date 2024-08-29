import pandas as pd
import string

def num_to_col_letters(num):
    letters = ''
    while num:
        mod = (num - 1) % 26
        letters += chr(mod + 65)
        num = (num - 1) // 26
    return ''.join(reversed(letters))

# Read the Excel file into a DataFrame
file_path = 'data.xlsx'
df = pd.read_excel(file_path)

# Define the Excel-style row index, column label, and value to insert
excel_row_index = 5         
excel_column_index = 10    
value = 10                 

# Convert Excel-style column label to DataFrame column index
# col_index = excel_column_label_to_index(excel_column_label)
# print(col_index)

# Ensure the DataFrame has enough columns
if excel_column_index >= len(df.columns):
    for _ in range(len(df.columns), excel_column_index + 1):
        df[f'NewColumn{_}'] = pd.NA  # Create a placeholder column if needed

# Convert Excel-style row index to DataFrame row index
row_index = excel_row_index - 1  # Convert to 0-based index

# Ensure the DataFrame has enough rows
if row_index >= len(df):
    # Append new rows with NA values for all columns
    df = df.reindex(range(row_index + 1))

# Set the value in the specified cell
df.iat[row_index, excel_column_index] = value

# Optionally: Save the modified DataFrame back to an Excel file
df.to_excel('modified_excel_file.xlsx', index=False, header=False)

print(df)
