#Script first written by paul from 
#http://pdwhomeautomation.blogspot.co.uk/2012/11/raspberry-pi-powered-lego-car.html
#Modified and updated by gbaman
#Version 0.1

# -*- coding: utf-8 -*-
#These are the keyboard mappings
#q = Go forward
#a = Stop going forward or back
#z = Go back
#i= Go left
#o = Stop steering
#p = Go right

#Get the GPIO module
import RPi.GPIO as GPIO

#Get the time module
import time

#Get the socket module
import socket

#Some IP constants for this, the server
UDP_IP = "192.168.1.2"
UDP_PORT= 8888

#A routine to control a pair of pins
def ControlAPairOfPins(FirstPin,FirstState,SecondPin,SecondState):
    print("Controlling pins")
    if FirstState == "1":
        GPIO.output(int(FirstPin),True)
    else:
        GPIO.output(int(FirstPin),False)
    if SecondState == "1":
        GPIO.output(int(SecondPin),True)
    else:
        GPIO.output(int(SecondPin),False)
            #Just retur
    return

####Main body of code

#Get rid of warnings
GPIO.setwarnings(False)

#Set the GPIO mode
GPIO.setmode(GPIO.BOARD)
#Set the pins to be outputs
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)

#Set up the IP related details
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

#Tell the user we've started
print "UDP server started.  Waiting for response...."

while True:
  #Wait for a UDP command to be received
    print("Waiting for UDP command")
    MyChar, addr = sock.recvfrom(1024) #buffer size is 1024
    print "I received: " + MyChar
    if MyChar == "q":
        ControlAPairOfPins("11","1","21","1")
        print "Forward"
    elif MyChar == "a":
        ControlAPairOfPins("19","0","21","0")
	ControlAPairOfPins("11","0","13","0")
        print "Stop"
    elif MyChar == "z":
        ControlAPairOfPins("13","1","19","1")
        print ("Back")
    elif MyChar == "i":
        ControlAPairOfPins("13","1","21","1")
        print "Left"
    elif MyChar == "o":
        ControlAPairOfPins("11","0","13","0")
	ControlAPairOfPins("19","0","21","0")
        print "Stop steering"
    elif MyChar == "p":
        ControlAPairOfPins("11","1","19","1")
        print "Right"
    else:
        print "Not a command"
