from pandas import *
import webbrowser
import urllib
from urllib.parse import quote_plus, quote, urlencode

l3 = []
csv_path_1 = 'C:\\Users\\Ksar01\\Desktop\\raw files\\16-04-2024.csv'
csv_path_2 = 'C:\\Users\\Ksar01\\Desktop\\raw files\\17-04-2024.csv'
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

original_list = l3
limit_size = 200
resulting_lists = [original_list[i:i + limit_size] for i in range(0, len(original_list), limit_size)]


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
    encoded_search_query = quote(SEARCH_QUERY, '()')
    # print(encoded_search_query)

    PARAMETERS = {'display.page.search.mode': 'fast',
                  'dispatch.sample_ratio': '1',
                  'display.page.search.tab': 'statistics',
                  'display.general.type': 'statistics'}
    full_url = f"{base_url}{encoded_search_query}&{urlencode(PARAMETERS)}"

    return full_url


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Total number of tracking numbers: ", len(l3))
    for i in resulting_lists:
        b = [str(num) for num in i]
        delimiter = " OR "
        result = delimiter.join(b)
        # print("Result: ", result, "\n")
        c = urlsplit(result)
        webbrowser.open(c)
