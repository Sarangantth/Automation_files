from pandas import *
import webbrowser

l3 = []
csv_path_1 = 'C:\\Users\\Ksar01\\Desktop\\raw files\\29-11-2023.csv'
csv_path_2 = 'C:\\Users\\Ksar01\\Desktop\\raw files\\30-11-2023.csv'
data_1 = read_csv(csv_path_1, sep=';')
data_2 = read_csv(csv_path_2, sep=';')
column_name_1 = 'Tracking Number'
column_data_1 = data_1[column_name_1].tolist()
column_name_2 = 'Tracking Number'
column_data_2 = data_2[column_name_2].tolist()

for item in column_data_2:
    if item in column_data_1:
        continue
    else:
        l3.append(item)

l3_str = [str(num) for num in l3]
delimiter = "%20OR%20"
result = delimiter.join(l3_str)
print("Result: ", result, "\n")
print("Total count of shipment tracking number: ", len(l3))

c=""
a="https://monitoring.sky.de/en-US/app/DA-Sky-Microservices/search?earliest=-30d%40d&latest=now&q=search%20index%3Dgcp_nc_prod%20("
b=")%20sourcetype%3D%22google%3Agcp%3Apubsub%3Amessage%22%20%22data.labels.k8s-pod%2Fservice_istio_io%2Fcanonical-name%22%3D%22naos-canonical-stream%22%20%20%20(%22iceCode%22%20%22ricCode%22%20%22stdEvent%22%20%22productCode%22%20%22trackingNumber%22)%20%0A%7Crex%20%22iceCode.%5C%22%5C%3A(%5Cs%2B%7C)(.%5C%22%7C)(%3F%3Cice_code%3E%5B%5E%5C%2C%5C%5C%5C%5D%2B)%22%0A%7Crex%20%22ricCode.%5C%22%5C%3A(%5Cs%2B%7C)(.%5C%22%7C)(%3F%3Cric_code%3E%5B%5E%5C%2C%5C%5C%5C%5D%2B)%22%0A%7Crex%20%22stdEvent.%5C%22%5C%3A(%5Cs%2B%7C)(.%5C%22%7C)(%3F%3Cstd_event_code%3E%5B%5E%5C%2C%5C%5C%5C%5D%2B)%22%0A%7Crex%20%22productCode.%5C%22%5C%3A(%5Cs%2B%7C)(.%5C%22%7C)(%3F%3Cproduct_code%3E%5B%5E%5C%2C%5C%5C%5C%5D%2B)%22%0A%7Crex%20%22%5C%22trackingNumber%5C%5C%5C.%5C%3A(%5Cs%2B%7C)%5C%5C%5C.(%3F%3CtrackingNumber%3E%5B%5E%5C%5C%5C%5D%2B)%22%0A%7Ctable%20_time%20ice_code%20ric_code%20std_event_code%20product_code%20trackingNumber%0A%7Cstats%20latest(ice_code)%20as%20ice_code%2C%20latest(ric_code)%20as%20ric_code%2C%20latest(std_event_code)%20as%20std_event_code%20latest(product_code)%20as%20product_code%20by%20trackingNumber&display.page.search.mode=fast&dispatch.sample_ratio=1&display.page.search.tab=statistics&display.general.type=statistics"
c= a + result + b
# print(c)
webbrowser.open(c)
