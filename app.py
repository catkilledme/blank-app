from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        location = request.form.get('location')
        if location:
            # Simulate a response with null (None) weather data
            weather_data = {
                'city': location,  # Return the city entered by the user
                'temperature': None,  # Simulate null temperature
                'description': None,  # Simulate null weather description
                'humidity': None,  # Simulate null humidity
                'pressure': None,  # Simulate null pressure
            }
            return render_template('index.html', weather_data=weather_data)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

@app.route('/', methods=['GET', 'POST'])
def home():
    print("Rendering template...")  # Debugging print
    if request.method == 'POST':
        location = request.form.get('location')
        if location:
            weather_data = {
                'city': location,
                'temperature': None,
                'description': None,
                'humidity': None,
                'pressure': None,
            }
            print(f"Weather Data: {weather_data}")  # Debugging print
            return render_template('index.html', weather_data=weather_data)
    
    return render_template('index.html')
