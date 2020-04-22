import requests

url = 'https://api.covid19api.com/world?from=2020-03-01T00:00:00Z&to=2020-04-01T00:00:00Z'


response = requests.get(url)

data = response.json()


print(data)