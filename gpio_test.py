import RPi.GPIO as GPIO
import time

gpio_start = 1
gpio_end = 27

GPIO.setmode(GPIO.BCM)

for x in range (gpio_start, gpio_end):
   GPIO.setup(x, GPIO.OUT)

while True:
   
   for y in range (gpio_start, gpio_end):
      GPIO.output(y, True)
      print 'on ', y
   time.sleep(.5)
   
   for z in range (gpio_start, gpio_end):
      GPIO.output(z, False)
      print 'off ',z
   time.sleep(.5)
