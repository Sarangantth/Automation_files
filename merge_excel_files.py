# import pandas as pd
#
# # Read the first CSV file
# df1 = pd.read_csv('file1.csv')
#
# # Read the second CSV file
# df2 = pd.read_csv('file2.csv')
#
# # Specify the rows and columns you want to merge
# # For example, to merge rows 1 and 2 from df1 and rows 3 and 4 from df2
# # and columns 'A' and 'B' from both dataframes
# merged_df = pd.concat([df1.iloc[1:3], df2.iloc[3:5]], axis=0)[['A', 'B']]


import pandas as pd
import openpyxl
from openpyxl.styles import NamedStyle


# Replace these with the paths to your CSV files
file1_path = 'C:\\Users\\Ksar01\\Downloads\\1.csv'
file2_path = 'C:\\Users\\Ksar01\\Downloads\\2.csv'
# file3_path = 'C:\\Users\\Ksar01\\Downloads\\3.csv'
# file4_path = 'C:\\Users\\Ksar01\\Downloads\\4.csv'
# file5_path = 'C:\\Users\\Ksar01\\Downloads\\5.csv'
# file6_path = 'C:\\Users\\Ksar01\\Downloads\\6.csv'
# file7_path = 'C:\\Users\\Ksar01\\Downloads\\7.csv'
# file8_path = 'C:\\Users\\Ksar01\\Downloads\\8.csv'

# Read data from each CSV file
df1 = pd.read_csv(file1_path)
df2 = pd.read_csv(file2_path)
# df3 = pd.read_csv(file3_path)
# df4 = pd.read_csv(file4_path)
# df5 = pd.read_csv(file5_path)
# df6 = pd.read_csv(file6_path)
# df7 = pd.read_csv(file7_path)
# df8 = pd.read_csv(file8_path)
# print(df1)

# Concatenate the rows from all three dataframes
merged_df = pd.concat([df1, df2], ignore_index=True)

# Replace 'your_excel_file.xlsx' with the path to your XLSX file
merged_df.to_excel('C:\\Users\\Ksar01\\Downloads\\01-01-2024.xlsx', index=False)
print("merged the shipment reports... \n" )
xlsx_file_path = 'C:\\Users\\Ksar01\\Downloads\\01-01-2024.xlsx'

# Load the Excel file
workbook = openpyxl.load_workbook(xlsx_file_path)

# Select the specific sheet you want to work with
sheet = workbook.active  # You can replace 'active' with the sheet name

# Define a custom number format style
number_format_style = NamedStyle(name='number_format_style')
number_format_style.number_format = '0'  # Customize the number format as needed

# Specify the column letter you want to format (e.g., 'A' for the first column)
column_letter = 'A'  # Replace with the desired column letter

# Iterate through the rows in the specified column and apply the custom number format style
for cell in sheet[column_letter]:
    cell.style = number_format_style

# Save the changes to the Excel file
workbook.save('C:\\Users\\Ksar01\\Downloads\\shipment report 17-04-2024.xlsx')

print(f"Number format for column {column_letter} has been updated.")
