from flask import Flask, render_template, request
import requests

app = Flask(__name__)
API_KEY = "b0d2c6aebdb2f9a87ccca74e8302178a"

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None

    if request.method == "POST":
        city = request.form["city"]
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {"q": city, "appid": API_KEY, "units": "metric"}

        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code == 200:
            weather = {
                "city": data["name"],
                "temp": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "desc": data["weather"][0]["description"].title()
            }
        else:
            weather = {"error": "City not found"}

    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)
