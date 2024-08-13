import cv2
import numpy as np
import serial

cap = cv2.VideoCapture("/dev/video2")
cap.set(3,640)
cap.set(4,489)
cap.set(10,100)

#ser = serial.Serial('/dev/ttyACM0',2000000)


while True:
 _,frame=cap.read()
 hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
 height,width,_=frame.shape
 
 cx=int(width/2)
 cy=int(height/2)
 
 piex_center=hsv_frame[cy,cx]
 hue_value=piex_center[0]
 s_value=piex_center[1]
 
 color = 0x100 #undefined

 can_buffer = [0x01, 0x40, 0x00]

 if s_value>70:
   if hue_value <5 :
        color =0x101 #"Red"
        can_buffer[2] = 1
   elif hue_value <22:
        color = 0x102 #"orenge"
        can_buffer[2] = 2
   elif hue_value<33:
        color = 0x103 #"Yellow"
        can_buffer[2] = 3
   elif hue_value<78:
        color = 0x104 #"Green"
        can_buffer[2] = 4
   elif hue_value <131:
        color = 0x105 #"Blue"
        can_buffer[2] = 5
   elif 167<= hue_value :
        color = 0x101 #"Red"
        can_buffer[2] = 1
    
   
   
   #ser.write(bytes(can_buffer))
   #ser.flush()
 
 
 cv2.circle(frame,(cx,cy),5,(25,25,25),3)
 
 
  
 cv2.imshow("Frame",frame)
 
 if cv2.waitKey(1) & 0xFF ==ord('q'):
    break
cap.release()
cv2.destroyAllWindows()

















