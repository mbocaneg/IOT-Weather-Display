import urequests
import ujson
from machine import Pin,I2C
import ssd1306

api_key = 'myapikey123456'
location = 'Chicago'

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=100000)
lcd = ssd1306.SSD1306_I2C(128,64,i2c)

r = urequests.get('http://api.openweathermap.org/data/2.5/weather?q=%s&units=imperial&APPID=%s' % (location, api_key))
response = r.json()
data = response['main']

#print("temp: " + str(data['temp']) + " °F" )
#print("humidity: " + str(data['humidity']) + " % ")


lcd.text("TEMP: " + str(data['temp']) + " F",0,0)
lcd.text("HUMIDITY: " + str(data['humidity']) + " % ",0,8)

lcd.show()
