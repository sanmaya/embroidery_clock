import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO_LED1 = 17
GPIO_LED2 = 18
GPIO_LED3 = 27
GPIO.setup(GPIO_LED1, GPIO.OUT)
GPIO.setup(GPIO_LED2, GPIO.OUT)
GPIO.setup(GPIO_LED3, GPIO.OUT)
try:
    while(1):
        GPIO.output(GPIO_LED1, GPIO.LOW) 
        GPIO.output(GPIO_LED2, GPIO.HIGH) 
        GPIO.output(GPIO_LED3, GPIO.LOW) 
        time.sleep(5)
        GPIO.output(GPIO_LED1, GPIO.HIGH) 
        GPIO.output(GPIO_LED2, GPIO.LOW) 
        GPIO.output(GPIO_LED3, GPIO.HIGH) 
        time.sleep(5)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
