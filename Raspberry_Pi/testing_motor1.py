import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.output(11,True)
sleep(0.5)
GPIO.output(11,False)
GPIO.output(13,True)
sleep(1)
GPIO.output(13,False)

GPIO.cleanup()
