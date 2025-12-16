import requests
import tkinter as tk

API_KEY = "b0d2c6aebdb2f9a87ccca74e8302178a"

def get_weather():
    city = city_entry.get()
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": API_KEY, "units": "metric"}

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code == 200:
        result = (
            f"City: {data['name']}\n"
            f"Temp: {data['main']['temp']} °C\n"
            f"Humidity: {data['main']['humidity']}%\n"
            f"Weather: {data['weather'][0]['description'].title()}"
        )
    else:
        result = "City not found!"

    result_label.config(text=result)

root = tk.Tk()
root.title("Weather App")

tk.Label(root, text="Enter City").pack()
city_entry = tk.Entry(root)
city_entry.pack()

tk.Button(root, text="Get Weather", command=get_weather).pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
