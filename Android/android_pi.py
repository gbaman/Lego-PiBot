#Script first written by paul from 
#http://pdwhomeautomation.blogspot.co.uk/2012/11/raspberry-pi-powered-lego-car.html
#Modified and updated by gbaman
#Version 0.1

import socket           
import time 
import android           

droid = android.Android() 

UDP_IP = '192.168.1.2'
UDP_PORT = 8888
INET_ADDR = (UDP_IP,UDP_PORT) 


MoveForward= "q" 
MoveBack = "z" 
MoveStop = "a" 
SteerLeft = "i" 
SteerRight = "p"
SteerStop = "o" 


ForwardThresh = 0.3
BackwardThresh = -0.3
LeftThresh = -0.3
RightThresh = 0.3

MoveState = MoveStop 
SteerState = SteerStop 

CurrentMove = "" 
CurrentSteer= "" 

print "UDP target IP:", UDP_IP 
print "UDP target port:", UDP_PORT 

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

droid.startSensingTimed(1, 250) 
time.sleep(1) 

while True: 
 try:   
   s1 = droid.sensorsReadOrientation().result   
    
        

   if s1[1] > ForwardThresh: 
     CurrentMove = MoveForward 
   elif s1[1] < BackwardThresh: 
     CurrentMove = MoveBack 
   else: CurrentMove = MoveStop 


   if s1[2] > RightThresh: 
     CurrentSteer = SteerRight 
   elif s1[2] < LeftThresh: 
     CurrentSteer = SteerLeft 
   else: CurrentSteer = SteerStop 

   if CurrentMove == MoveState: 
     CurrentMove = CurrentMove 
   else: 
     MoveState = CurrentMove 
     sock.sendto(CurrentMove, INET_ADDR) 
     print "Forward / back state changed.  Sent: " + CurrentMove       
    
   if CurrentSteer == SteerState: 
     CurrentSteer = CurrentSteer     
   else: 
     SteerState = CurrentSteer 
     sock.sendto(CurrentSteer, INET_ADDR)       
     print "Left / right state changed.  Sent: " + CurrentSteer 
  
     time.sleep(1) 
 except Exception, err: 
   print "Got us an exception: " + str(err)   
   time.sleep(1)
