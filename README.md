# IOT-Weather-Display
An IOT weather display based on the ESP32 MCU and an SSD1306 LCD. The language
of choice for this project is MicroPython. The code structure is fairly straightforward:
A REST URI is constructed by concatenating a base URI(from the OpenWeathermap REST API), 
with a user's location and API key. Next, a REST call is issued to said URI, where its
response is stored in a Micropython JSON object. Finally, "temperature" and "humidity"
fields of this JSON object are extracted and displayed onto an SSD1306 OLED(through the
use of Micropython's ssd1306 library).
