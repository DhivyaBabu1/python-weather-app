import requests

API_KEY = "b0d2c6aebdb2f9a87ccca74e8302178a"

def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": API_KEY, "units": "metric"}

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code == 200:
        print("\n🌦 Weather Report")
        print("----------------------")
        print("City:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Condition:", data["weather"][0]["description"].title())
    else:
        print("❌ City not found")

while True:
    city = input("\nEnter city (or exit): ")
    if city.lower() == "exit":
        break
    get_weather(city)
