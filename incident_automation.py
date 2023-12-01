import pandas as pd

# Replace 'your_excel_file.xlsx' with the path to your Excel file
e1 = "C:\Workspace\demo_incident\incident.xlsx"
e2 = "C:\Workspace\demo_incident\incident(1).xlsx"
e3 = "C:\Workspace\demo_incident\incident.xlsx"
e4 = "C:\Workspace\demo_incident\incident(1).xlsx"

# Load the Excel file into a Pandas DataFrame
d1 = pd.read_excel(e1)
d2 = pd.read_excel(e2)
# Display the first few rows of the DataFrame
# print(d1.head(),'\n')
f1 = d1[['Number']]
print(f1,'\n')
f2 = d2.iloc[:, 0]
print(f2)
# You can now work with the data in the DataFrame
# For example, you can access specific columns like this:
# column_data = df['Column_Name']

# Or filter the data based on conditions:
# filtered_data = df[df['Column_Name'] > 50]

# Or perform various data analysis and manipulation tasks
