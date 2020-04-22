import requests
import json



url_Summary = 'https://api.covid19api.com/summary'
url_All='https://api.covid19api.com/country/united-states/status/confirmed/live'


response_Summary = requests.get(url_Summary)
response_All = requests.get(url_All)


data_Summary = response_Summary.json()
data_All = response_All.json()


print("Summary:", data_All[1]['Cases'])

length_All = len(data_All)
length_Summary = len(data_Summary)


# newdata = json.dumps(data['Countries'][1]['NewConfirmed'], separators=(',', ':'))
# newnew =int(newdata)

# print(newnew)

for x in range(length_Summary):
    if int(json.dumps(data_Summary['Countries'][x]['NewConfirmed'], separators=(',', ':'))) >= 1:
       print(data_Summary['Countries'][x]['Country'] + ":",data_Summary['Countries'][x]['NewConfirmed']) 


for x in range(length_All):
    if int(json.dumps(data_All[x]['Cases'], separators=(',', ':'))) >= 1:
       print( data_All[x]['Province'] + ":" + data_All[x]['City'] + " Cases today:" + str(data_All[x]['Cases'])
        + " Lat:" +str(data_All[x]['Lat']) + " Lon:" + str(data_All[x]['Lon'])
       )

# json_data = json.dumps(data["Country": "Israel"], separators=(',', ':'))

# json_object = json.loads(json_data)

# json_formatted_str = json.dumps(json_object, indent=2)

# print(json_formatted_str)