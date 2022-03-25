import os
import sys
import gettext
import requests



def setup_i18n(domain, localedir):
    gettext.bindtextdomain(domain, localedir)
    gettext.textdomain(domain)


def fetch_env_key(key):
    api_key = os.getenv(key)
    if not api_key:
        raise ValueError(_('Set environment variable "%s" ' % key)
                         + _('to gain access to OpenWeather API.'))
    return api_key


def fetch_weather_data(city):
    response = {}
    try:
        response = requests.get('https://api.openweathermap.org/data/2.5/'
                                f'weather?q={city}&units=metric&appid={api_key}').json()
        # print("Weather data from {}: {}".format(city, response))
    except ConnectionError:
        print(_('Can not connect to the internet.'))

    if int(response['cod']) != 200:
        print('Som tin went wong: %s, city was %s' % (response['message'], city))

    return response



setup_i18n(r'weather', r'./locale')
_ = gettext.gettext

print(_('This is a translatable text.'))

api_key = fetch_env_key('WEATHER_API_KEY')

cities = sys.argv[1:]

answer = _('Light beerlamps{yes_or_no} at {city}.')
does_not = _(' NOT')

for city in cities:
    response = fetch_weather_data(city)

    condition = response['weather'][0]['main']
    temperature = int(response['main']['temp'])

    yes_or_no = ''
    if condition != 'Clear' or temperature <= 10:
        yes_or_no = does_not

    ##DEBUG print(f'Debug Cond: {condition}, Temperature: {temperature}')
    print(answer.format(yes_or_no = yes_or_no, city = city))
