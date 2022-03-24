import sys
import os
import gettext
import requests

localedir = r'./locale'

gettext.bindtextdomain('weather', localedir)
gettext.textdomain('weather')
_ = gettext.gettext

print(_("This is a translatable text."))

api_key = os.getenv('WEATHER_API_KEY')
if not api_key:
    raise ValueError(_('Set environment variable "WEATHER_API_KEY" ')
                     + _('to gain access to OpenWeather API.'))

city = sys.argv[1]
response = {}
try:
    response = requests.get('https://api.openweathermap.org/data/2.5/'
                            f'weather?q={city}&units=metric&appid={api_key}').json()
    print( "Weather data from {}: {}".format( city, response))
except ConnectionError:
    print(_('Can not connect to the internet.'))
condition = response['weather'][0]['main']
temperature = int(response['main']['temp'])

answer = _('Light beerlamps{yes_or_no} at {city}.')
does_not = _(' NOT')
yes_or_no = ''
if condition != 'Clear' or temperature <= 10:
    yes_or_no = does_not

print(answer.format(yes_or_no = yes_or_no, city = city))
