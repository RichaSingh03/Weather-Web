from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

def get_weather_data(api_key, city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = json.loads(response.text)
    return data

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        api_key = "c6e69bb49acdf55dfb95838d9d9e7b17"
        weather_data = get_weather_data(api_key, city)

        if weather_data['cod'] == '404':
            return render_template('index.html', error="City not found.")
        else:
            temperature = weather_data['main']['temp']
            description = weather_data['weather'][0]['description']
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']

            return render_template('index.html',city=city, temperature=temperature, description=description,
                                   humidity=humidity, wind_speed=wind_speed)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
