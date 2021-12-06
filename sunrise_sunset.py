import requests

LATITUDE = 19.075983
LONGITUDE = 72.877655
parameters = {
    "lat": LATITUDE,
    "lng": LONGITUDE,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
sunrise = response.json()["results"]["sunrise"]
print(sunrise.split("T")[1].split(":")[0])
response.raise_for_status()

data = response.json()
print(data)