from flask import Flask, render_template, request
from weather import main as get_weather

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    my_data = None
    friend_data = None
    comparison_message = None

    if request.method == 'POST':
        # Retrieve hidden field values for persisting data
        my_data = {
            "name": request.form.get("myCityName", ""),
            "temperature": int(request.form.get("myTemperature", 0) or 0),
            "description": request.form.get("myDescription", ""),
            "icon": request.form.get("myIcon", ""),
            "humidity": int(request.form.get("myHumidity", 0) or 0)
        } if request.form.get("myCityName") else None

        friend_data = {
            "name": request.form.get("friendCityName", ""),
            "temperature": int(request.form.get("friendTemperature", 0) or 0),
            "description": request.form.get("friendDescription", ""),
            "icon": request.form.get("friendIcon", ""),
            "humidity": int(request.form.get("friendHumidity", 0) or 0)
        } if request.form.get("friendCityName") else None

        # Process form inputs for new data
    if request.form.get('myCityName'):
        my_city = request.form.get('myCityName', '').strip()
        my_state = request.form.get('myStateName', '').strip()
        my_country = request.form.get('myCountryName', '').strip()
        if my_city:
            my_data = get_weather(my_city, my_state, my_country).__dict__

    if request.form.get('friendCityName'):
        friend_city = request.form.get('friendCityName', '').strip()
        friend_state = request.form.get('friendStateName', '').strip()
        friend_country = request.form.get('friendCountryName', '').strip()
        if friend_city:
            friend_weather = get_weather(friend_city, friend_state, friend_country)
            if friend_weather:
                friend_data = friend_weather.__dict__
    print(my_data)
    print(friend_data)
    # Perform comparison if both datasets are available
    if my_data and friend_data:
        temp_diff = my_data["temperature"] - friend_data["temperature"]
        humid_diff = my_data["humidity"] - friend_data["humidity"]

        comparison_message = f"It's {abs(temp_diff)}°C {'hotter' if temp_diff > 0 else 'cooler'} where you are. "
        comparison_message += f"The air is {abs(humid_diff)}% {'more humid' if humid_diff > 0 else 'less humid'} where you are."

    return render_template('index.html', myData=my_data, friendData=friend_data, comparisonMessage=comparison_message)

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        # Handle settings form submissions later
        pass
    return render_template('settings.html')

if __name__ == "__main__":
    app.run(debug=True)
