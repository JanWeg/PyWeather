# A simple call to openweathermap api 

What is the weather like in ...

OpenWeatherMap website offers an api to fetch the weather data from many different location in the world.

# call
```shell
$ LANGUAGE=de python3 weather.py Gothenburg
 Dies ist ein übersetzbarer Text.
 Weather data from Gothenburg: {'coord': {'lon': 11.9668, 'lat': 57.7072}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'base': 'stations', 'main': {'temp': 7.53, 'feels_like': 4.91, 'temp_min': 6.77, 'temp_max': 8.71, 'pressure': 1026, 'humidity': 73}, 'visibility': 10000, 'wind': {'speed': 4.12, 'deg': 270}, 'clouds': {'all': 0}, 'dt': 1648142222, 'sys': {'type': 2, 'id': 2002867, 'country': 'SE', 'sunrise': 1648098204, 'sunset': 1648143204}, 'timezone': 3600, 'id': 2711537, 'name': 'Gothenburg', 'cod': 200}
 Zünden Sie die Bierlichter in Gothenburg NICHT an.
```

```shell
$ LANGUAGE=sv python3 weather.py Athens
 Detta är en översättningsbar text.
 Weather data from Athens: {'coord': {'lon': 23.7162, 'lat': 37.9795}, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}], 'base': 'stations', 'main': {'temp': 14.27, 'feels_like': 12.72, 'temp_min': 11.99, 'temp_max': 15.66, 'pressure': 1020, 'humidity': 37}, 'visibility': 10000, 'wind': {'speed': 1.34, 'deg': 159, 'gust': 2.24}, 'clouds': {'all': 20}, 'dt': 1648142317, 'sys': {'type': 2, 'id': 2018805, 'country': 'GR', 'sunrise': 1648095775, 'sunset': 1648139995}, 'timezone': 7200, 'id': 264371, 'name': 'Athens', 'cod': 200}
 Öllampan lyser INTE i Athens.
```

# Internationalization (i18n/l10n)

The pytonfile- when interpreted, contains strings like 'Hello World!' and usually are printed literally. 
If you want them to print according to the current locale, you can use python's gettext module.

```python
gettext.bindtextdomain('weather', 'locale')
gettext.textdomain('weather')
_ = gettext.gettext
```

As described in many how-to's I use .POT-Files (Portable Object Template).
Basicaly it consists of a MessageID and a MessageText.
To extract the strings relevant for translation you mark every string with the above Underscore ("_").
So, if you want to translate 'Hello World!' you put it as _('Hello World!) into the python-file. Now 'Hello World!' is
the message key.

When all translatable strings are marked in the above way, you run
```python
$> pygettext3 -d weather weather.py
```
This will produce a weather.pot file with some dummy project information and
>\#: weather.py: ~lineno~
> 
>msgid "This is a translatable text."
> 
>msgstr ""

And yes, no translation here (yet).

Grab the poeditor (there is a free version available) and translate it to a language of your choice.
It will help you with translations from google-translator. 
And finally it will produce the needed translations (.po and .mo files).

Provided, that you have set the domain to 'weather'
and the language to e.g. 'sv' then you have to create a directory 
'locale/sv/LC_MESSAGES/' within your project and place the resulting .po and .mo here (you do that by saving the
translation results from the poeditor)
Thisignore way you can create as many translations as you want.

To switch the output language, one must prefix the python command with
```LANGUAGE=YZ```, where YZ is the ISO-Code of your preferred country/language 
if the translation is not present, the default translation (from the python file) will be used.

