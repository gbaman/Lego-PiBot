import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.output(21,True)
sleep(0.5)
GPIO.output(21,False)
GPIO.output(19,True)
sleep(0.5)
GPIO.output(19,False)

GPIO.cleanup()
