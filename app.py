import requests

api_key = '09118d9f8d6629d10ca73bfece254da6'

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/onecall?lat=49.21&lon=-123.03&appid={api_key}")

sunrise = weather_data.xml()['sys']['sunrise']
sunset = weather_data.xml()['sys']['sunset']
timezone = weather_data.xml()['sys']['timezone']

print(weather_data)
