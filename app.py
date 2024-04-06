from flask import Flask, render_template, request, jsonify
import urllib.request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    data = request.json
    city = data['city']
    api_key = "fa9a66e895256601c224af015218519f" 

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode('utf-8'))

    if data["cod"] == 200:
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        result = f"Weather in {city}:<br>"
        result += f"Description: {weather_description}<br>"
        result += f"Temperature: {temperature}°C<br>"
        result += f"Feels like: {feels_like}°C<br>"
        result += f"Humidity: {humidity}%<br>"
        result += f"Wind Speed: {wind_speed} m/s"
    else:
        result = "City not found."

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
