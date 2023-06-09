import requests
import time
from wallpaper import Wallpaper

api_key = '09118d9f8d6629d10ca73bfece254da6'

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q=Vancouver&APPID={api_key}")

#given in unix, UTC
sunrise = weather_data.json()['sys']['sunrise']
sunset = weather_data.json()['sys']['sunset']
timezone = weather_data.json()['timezone']

print(sunrise)
print(sunset)
print(timezone)

#also in unix, UTC
curr_time = time.time()
print(curr_time)

if curr_time < sunrise:
    #set wallpaper to presunrise
    print()
elif sunrise - 900 < curr_time < sunrise + 900:
    #set wallpaper to sunrise
    print()
elif sunrise + 900 <= curr_time <= sunset - 1800:
    #set wallpaper to daytime
    Wallpaper.setWallpaper(Wallpaper, Wallpaper.wallpapers["TOKYO"])
    print("set daytime")
elif sunset - 1800 < curr_time < sunset + 1800:
    #set wallpaper to daytime
    print()

