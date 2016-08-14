import time
import urllib.request
import json
import re
import RPi.GPIO as GPIO

url = 'http://api.openweathermap.org/data/2.5/weather?'

GPIO.setmode(GPIO.BCM)

GPIO_CLEAR = 17
GPIO_CLOUD = 18
GPIO_RAIN  = 27

GPIO.setup(GPIO_CLEAR, GPIO.OUT)
GPIO.setup(GPIO_CLOUD, GPIO.OUT)
GPIO.setup(GPIO_RAIN,  GPIO.OUT)

GPIO.output(GPIO_CLEAR, GPIO.HIGH) 
GPIO.output(GPIO_CLOUD, GPIO.HIGH) 
GPIO.output(GPIO_RAIN,  GPIO.HIGH) 

try:
    while(1):
        response = urllib.request.urlopen(url)
        encoding = response.headers.get_content_charset()
        line = response.read().decode(encoding)

        print("Line: " + line)

        pattern = re.compile(r'\d+')
        decode = json.loads(line)
        weather = decode['weather'][0]['main']

        print("Weather: " + weather)

        if weather == "Clear":
            GPIO.output(GPIO_CLEAR, GPIO.LOW) 
            GPIO.output(GPIO_CLOUD, GPIO.HIGH) 
            GPIO.output(GPIO_RAIN,  GPIO.HIGH) 

        if weather == "Clouds":
            GPIO.output(GPIO_CLEAR, GPIO.HIGH) 
            GPIO.output(GPIO_CLOUD, GPIO.LOW) 
            GPIO.output(GPIO_RAIN,  GPIO.HIGH) 

        if weather == "Rain" or weather == "Snow":
            GPIO.output(GPIO_CLEAR,  GPIO.HIGH) 
            GPIO.output(GPIO_CLOUD,  GPIO.HIGH) 
            GPIO.output(GPIO_RAIN,   GPIO.LOW) 

        time.sleep(100)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
