import urllib
from urllib.parse import quote_plus, quote, urlencode
from pandas import *
import webbrowser
l1 = []
l2 = []
l3 = []
csv_path_1 = 'C:\\Users\\Ksar01\\Desktop\\raw files\\26-11-2023.csv'
csv_path_2 = 'C:\\Users\\Ksar01\\Desktop\\raw files\\28-11-2023.csv'
csv_path_3 = 'C:\\Users\\Ksar01\\Desktop\\raw files\\29-11-2023.csv'
csv_path_4 = 'C:\\Users\\Ksar01\\Desktop\\raw files\\30-11-2023.csv'
data_1 = read_csv(csv_path_1, sep=';')
data_2 = read_csv(csv_path_2, sep=';')
data_3 = read_csv(csv_path_3, sep=';')
data_4 = read_csv(csv_path_4, sep=';')
column_name_1 = 'Tracking Number'
column_data_1 = data_1[column_name_1].tolist()
column_name_2 = 'Tracking Number'
column_data_2 = data_2[column_name_2].tolist()
column_name_3 = 'Tracking Number'
column_data_3 = data_1[column_name_3].tolist()
column_name_4 = 'Tracking Number'
column_data_4 = data_1[column_name_4].tolist()

for item in column_data_2:
    if item in column_data_1:
        continue
    else:
        l1.append(item)
# print(len(l1))

for item in l1:
    if item in column_data_3:
        continue
    else:
        l2.append(item)
for i in l2:
    column_data_3.append(i)


for item in column_data_3:
    if item in column_data_4:
        continue
    else:
        l3.append(item)
for j in l3:
    column_data_4.append(j)


print("Total number of tracking numbers: ",len(column_data_4))
original_list=column_data_4
limit_size = 200
resulting_lists = [original_list[i:i + limit_size] for i in range(0, len(original_list), limit_size)]
# print(resulting_lists)

def urlsplit(result):
    SEARCH_QUERY = f"""index=gcp_nc_prod ({result}) sourcetype="google:gcp:pubsub:message" "data.labels.k8s-pod/service_istio_io/canonical-name"="naos-canonical-stream"   ("iceCode" "ricCode" "stdEvent" "productCode" "trackingNumber") 
|rex "iceCode.\\"\:(\s+|)(.\\"|)(?<ice_code>[^\,\\\\\]+)"
|rex "ricCode.\\"\:(\s+|)(.\\"|)(?<ric_code>[^\,\\\\\]+)"
|rex "stdEvent.\\"\:(\s+|)(.\\"|)(?<std_event_code>[^\,\\\\\]+)"
|rex "productCode.\\"\:(\s+|)(.\\"|)(?<product_code>[^\,\\\\\]+)"
|rex "\\"trackingNumber\\\\\.\:(\s+|)\\\\\.(?<trackingNumber>[^\\\\\]+)"
|table _time ice_code ric_code std_event_code product_code trackingNumber
|stats latest(ice_code) as ice_code, latest(ric_code) as ric_code, latest(std_event_code) as std_event_code latest(product_code) as product_code by trackingNumber"""

    base_url = """https://monitoring.sky.de/en-US/app/DA-Sky-Microservices/search?earliest=-30d%40d&latest=now&q=search%20"""
    encoded_search_query = quote(SEARCH_QUERY,'()')
# print(encoded_search_query)

    PARAMETERS = {'display.page.search.mode': 'fast',
              'dispatch.sample_ratio': '1',
              'display.page.search.tab': 'statistics',
              'display.general.type': 'statistics'}
    full_url = f"{base_url}{encoded_search_query}&{urlencode(PARAMETERS)}"

    return full_url


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



if __name__ == '__main__':
    for i in resulting_lists:
        b = [str(num) for num in i]
        delimiter = " OR "
        result = delimiter.join(b)
        # print("Result: ", result, "\n")
        c=urlsplit(result)
        webbrowser.open(c)



