import urequests
import ujson
from machine import Pin,I2C
import ssd1306

#user's custom API key, as well as a desired location
api_key = 'myapikey123456'
location = 'Chicago'

#set up I2C pins, and bind an ssd1306 instance to these pins
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=100000)
lcd = ssd1306.SSD1306_I2C(128,64,i2c)

#concatenate user's API key and location with an OpenWeatherMap URI, and issue a REST call
r = urequests.get('http://api.openweathermap.org/data/2.5/weather?q=%s&units=imperial&APPID=%s' % (location, api_key))

#store the response in a JSON object, and extract relevant data
response = r.json()
data = response['main']

#print("temp: " + str(data['temp']) + " °F" )
#print("humidity: " + str(data['humidity']) + " % ")

#Extract temperature and humidity fields, and display onto OLED
lcd.text("TEMP: " + str(data['temp']) + " F",0,0)
lcd.text("HUMIDITY: " + str(data['humidity']) + " % ",0,8)

lcd.show()
