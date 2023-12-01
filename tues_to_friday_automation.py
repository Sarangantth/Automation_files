from pandas import *
import webbrowser
import urllib
from urllib.parse import quote_plus, quote, urlencode

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
delimiter = " OR "
result = delimiter.join(l3_str)
print("Result: ", result, "\n")
print("Total count of shipment tracking number: ", len(l3))


SEARCH_QUERY = f"""index=gcp_nc_prod ({result}) sourcetype="google:gcp:pubsub:message" "data.labels.k8s-pod/service_istio_io/canonical-name"="naos-canonical-stream"   ("iceCode" "ricCode" "stdEvent" "productCode" "trackingNumber") 
|rex "iceCode.\\"\:(\s+|)(.\\"|)(?<ice_code>[^\,\\\\\]+)"
|rex "ricCode.\\"\:(\s+|)(.\\"|)(?<ric_code>[^\,\\\\\]+)"
|rex "stdEvent.\\"\:(\s+|)(.\\"|)(?<std_event_code>[^\,\\\\\]+)"
|rex "productCode.\\"\:(\s+|)(.\\"|)(?<product_code>[^\,\\\\\]+)"
|rex "\\"trackingNumber\\\\\.\:(\s+|)\\\\\.(?<trackingNumber>[^\\\\\]+)"
|table _time ice_code ric_code std_event_code product_code trackingNumber
|stats latest(ice_code) as ice_code, latest(ric_code) as ric_code, latest(std_event_code) as std_event_code latest(product_code) as product_code by trackingNumber"""

BASE_URL = """https://monitoring.sky.de/en-US/app/DA-Sky-Microservices/search?earliest=-30d%40d&latest=now&q=search
%20"""

PARAMETERS = {'display.page.search.mode': 'fast',
             'dispatch.sample_ratio': '1',
             'display.page.search.tab': 'statistics',
             'display.general.type': 'statistics'}

def print_hi(name):
   # Use a breakpoint in the code line below to debug your script.
   print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def url_encode(query_string):
   return quote(query_string, '()')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   print_hi('Sarangantth')
   f = url_encode(SEARCH_QUERY)
   c = BASE_URL + f + '&' + urlencode(PARAMETERS)
   print(c)
   webbrowser.open(c)