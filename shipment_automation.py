from pandas import *
import webbrowser
# import xlwt
import csv
# import openpyxl

l3 = []
c=0
# row_count=0
# column_count=0

csv_path_1 = 'C:\\Users\\Ksar01\\Desktop\\raw files\\21-11-2023.csv'
csv_path_2 = 'C:\\Users\\Ksar01\\Desktop\\raw files\\22-11-2023.csv'
data_1 = read_csv(csv_path_1, sep=';')
data_2 = read_csv(csv_path_2, sep=';')
column_name_1 = 'Tracking Number'
column_data_1 = data_1[column_name_1].tolist()
column_name_2 = 'Tracking Number'
column_data_2 = data_2[column_name_2].tolist()

# output_xlsx = 'C:\\Users\\Ksar01\\PycharmProjects\\pythonProject\\output.xlsx'
# # data_2.to_excel(output_xlsx, index=False)
#
# # with open(csv_path_2, 'r', newline='') as csvfile:
# #     csv_reader = csv.reader(csvfile)
# #     for row in csv_reader:
# #         row_count += 1
# #         column_count = max(column_count, len(row))
# #
# #
# # print(row_count, "\n")
# # print(column_count, "\n")
#
# # Open the Excel file
# workbook = openpyxl.load_workbook(output_xlsx, read_only=True)
#
# # Select the active sheet (you can specify a specific sheet if needed)
# sheet = workbook.active
#
# # Find the number of rows and columns
# num_rows = sheet.max_row
# num_columns = sheet.max_column
#
# print(f"Number of rows: {num_rows}")
# print(f"Number of columns: {num_columns}")


for item in column_data_2:
    if item in column_data_1:
        continue
    else:
        l3.append(item)
        c+=1
print("Total count of shipment tracking number: ", len(l3))
l3_str = [str(num) for num in l3]
delimiter = "%20OR%20"
result = delimiter.join(l3_str)
print("Result: ", result, "\n")
# print(type(l3_str))
print("Total count of shipment tracking number: ", c)
c=""
a="https://monitoring.sky.de/en-US/app/DA-Sky-Microservices/search?earliest=-30d%40d&latest=now&q=search%20index%3Dgcp_nc_prod%20("
b=")%20sourcetype%3D%22google%3Agcp%3Apubsub%3Amessage%22%20%22data.labels.k8s-pod%2Fservice_istio_io%2Fcanonical-name%22%3D%22naos-canonical-stream%22%20%20%20(%22iceCode%22%20%22ricCode%22%20%22stdEvent%22%20%22productCode%22%20%22trackingNumber%22)%20%0A%7Crex%20%22iceCode.%5C%22%5C%3A(%5Cs%2B%7C)(.%5C%22%7C)(%3F%3Cice_code%3E%5B%5E%5C%2C%5C%5C%5C%5D%2B)%22%0A%7Crex%20%22ricCode.%5C%22%5C%3A(%5Cs%2B%7C)(.%5C%22%7C)(%3F%3Cric_code%3E%5B%5E%5C%2C%5C%5C%5C%5D%2B)%22%0A%7Crex%20%22stdEvent.%5C%22%5C%3A(%5Cs%2B%7C)(.%5C%22%7C)(%3F%3Cstd_event_code%3E%5B%5E%5C%2C%5C%5C%5C%5D%2B)%22%0A%7Crex%20%22productCode.%5C%22%5C%3A(%5Cs%2B%7C)(.%5C%22%7C)(%3F%3Cproduct_code%3E%5B%5E%5C%2C%5C%5C%5C%5D%2B)%22%0A%7Crex%20%22%5C%22trackingNumber%5C%5C%5C.%5C%3A(%5Cs%2B%7C)%5C%5C%5C.(%3F%3CtrackingNumber%3E%5B%5E%5C%5C%5C%5D%2B)%22%0A%7Ctable%20_time%20ice_code%20ric_code%20std_event_code%20product_code%20trackingNumber%0A%7Cstats%20latest(ice_code)%20as%20ice_code%2C%20latest(ric_code)%20as%20ric_code%2C%20latest(std_event_code)%20as%20std_event_code%20latest(product_code)%20as%20product_code%20by%20trackingNumber&display.page.search.mode=fast&dispatch.sample_ratio=1&display.page.search.tab=statistics&display.general.type=statistics"
c= a + result + b
print(c)
webbrowser.open(c)

# data = []
# with open(csv_path_2, 'r', newline='') as csvfile:
#     csv_reader = csv.reader(csvfile)
#     data = [row for row in csv_reader]

# Add the string to the data
# new_row = [result]
# data.append(new_row)
#
# # Write the updated data back to the CSV file
# with open(csv_path_2, 'w', newline='') as csvfile:
#     csv_writer = csv.writer(csvfile)
#     csv_writer.writerows(data)
#
# print("Changes have been saved to the CSV file.")

# with open(csv_path_2, 'w+', newline='') as csvfile:
#     csv_writer = csv.writer(csvfile)
#
#     # Write the string as a new row
#     csv_writer.writerow([result])

# wb = xlwt.Workbook()
# sheet = wb.add_sheet("output_xlsx")
# r=0
# c=0
# sheet.write(r,c,result)
# wb.save("output.xls")





