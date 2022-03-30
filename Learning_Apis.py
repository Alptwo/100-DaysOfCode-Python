import datetime
import requests

# response = requests.get(url = "http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()["iss_position"]["longitude"]

# print(data)
parameters = {
    "lat": 51.507,
    "lng": -0.127758,
    "formatted": 0
}


response = requests.get("https://api.sunrise-sunset.org/json", params = parameters)
response.raise_for_status()

data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)