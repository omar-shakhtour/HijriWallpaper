from wallpaper import set_wallpaper, get_wallpaper
from PIL import Image, ImageDraw, ImageFont
from hijridate import Hijri
from time import gmtime, strftime
from datetime import date
from datetime import datetime
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from suntime import Sun

# ------------------ Location & Time Calculations ------------------#

# Nominatim API to get latitude and longitude
geolocator = Nominatim(user_agent="at")

# input place
place = "charlotte"
location = geolocator.geocode(place)

# coordinates
latitude = location.latitude
longitude = location.longitude
coordinates = Sun(latitude, longitude)

# Local sunrise time calculation
time_zone = date(2023, 4, 25)
dateSunset = coordinates.get_local_sunset_time(time_zone)
sunset = dateSunset.strftime('%H:%M')

# Local current time
dateCurrentTime = datetime.now()
currentTime = dateCurrentTime.strftime('%H:%M')
print(sunset)
print(currentTime)

# display
print("Current time at : ", currentTime)
print("Sunset at : ", sunset)

# ------------------ Image Processing ------------------ #

# Open image from folder
file = "C://Users/oshak/OneDrive/Desktop/backgroundImage/Sunflower.jpg"
dayImg = Image.open(file)

file = "C://Users/oshak/OneDrive/Desktop/backgroundImage/Macaw.jpg"
nightImg = Image.open(file)

# Make a draw object
draw = ImageDraw.Draw(dayImg)
drawNight = ImageDraw.Draw(nightImg)

# Get today's date from the Islamic calendar
hijri = Hijri.today().isoformat()

# Change the font
font = ImageFont.truetype('arial.ttf', 162)

draw.text((500, 500), hijri, font=font, fill='black')
drawNight.text((500, 500), hijri, font=font, fill='white')

# ------------------ Change Wallpaper Based on Time of Day ------------------
if (currentTime < sunset):
    dayImg.save()

else:
    print("Current")
    print(currentTime)
    print("info")
    print(sunset)
    nightImg.show()
