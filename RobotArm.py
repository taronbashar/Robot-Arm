import cv2
import sys
import numpy as np
import time
import meArm
   
####################
#Start of camera use
#place camera 21 inches back
####################
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(2)
camera.stop_preview()
camera.close()

R1=''
R2=''
R3=''
camera_num = 0  # usually 0
exposure = -1   # automatic exposure -1 
width = 320     # 640, 1920
height = 240    # 480, 1080
fps=30          # 
fourcc = ''     # 'YUY2', 'MPEG' 
output_res = (320, 240)
i=0
######
# Open the camera with platform optimal settings
if sys.platform.startswith('win'):
    capture = cv2.VideoCapture(camera_num, apiPreference=cv2.CAP_MSMF)
elif sys.platform.startswith('darwin'):
    capture = cv2.VideoCapture(camera_num, apiPreference=cv2.CAP_AVFOUNDATION)
elif sys.platform.startswith('linux'):
    capture = cv2.VideoCapture(camera_num, apiPreference=cv2.CAP_V4L2)
else:
    capture = cv2.VideoCapture(camera_num, apiPreference=cv2.CAP_ANY)
# Set Camera
capture.set(cv2.CAP_PROP_FRAME_WIDTH,width)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
if exposure < 0:
    capture.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1)
else:
    capture.set(cv2.CAP_PROP_EXPOSURE,exposure)
capture.set(cv2.CAP_PROP_FPS, fps)
capture.set(cv2.CAP_PROP_BUFFERSIZE, 4)
if fourcc: 
    fourccnumber=cv2.VideoWriter_fourcc(fourcc[0],fourcc[1],fourcc[2],fourcc[3])
    capture.set(cv2.CAP_PROP_FOURCC, fourccnumber)
# Read Camera Properties
frameRate  = capture.get(cv2.CAP_PROP_FPS)
brightness = capture.get(cv2.CAP_PROP_BRIGHTNESS)
contrast   = capture.get(cv2.CAP_PROP_CONTRAST)
saturation = capture.get(cv2.CAP_PROP_SATURATION)
# Open Window to show camera. If users closes window, program stops
window_handle = cv2.namedWindow("Camera")
while(cv2.getWindowProperty("Camera", 0) >= 0):
    # Read Image
    _, img = capture.read()
    # Resize image
    tmp = cv2.resize(img, output_res)
    # Convert from BGR to HSV
    hsv = cv2.cvtColor(tmp, cv2.COLOR_BGR2HSV)
    hue=hsv[:,:,0]
    sat=hsv[:,:,1]
    val=hsv[:,:,2]
    # Threshold for the brightest objects, optional
    # Adjust if you want to threshold for your game piece
    thresholded = cv2.inRange(hsv, (0,0,254),(255,255,255) )
    ####
    # Show area of interest
    # Calculate average intensity, saturation and hue in ROI
    c1=200
    c2=150
    w2=35
    ROI=val[c1-w2:c1+w2,c2-w2:c2+w2]
    V=np.sum(ROI, dtype=np.uint32)/(2*w2+1)/(2*w2+1)
    ROI=sat[c1-w2:c1+w2,c2-w2:c2+w2]
    S=np.sum(ROI, dtype=np.uint32)/(2*w2+1)/(2*w2+1)
    ROI=hue[c1-w2:c1+w2,c2-w2:c2+w2]
    H=np.sum(ROI, dtype=np.uint32)/(2*w2+1)/(2*w2+1)
    tmp = cv2.putText(tmp, f"H:{H:3.1f} S:{S:3.1f} V:{V:3.1f}" , (c2-w2, c1+3*w2), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1, cv2.LINE_AA)
    cv2.rectangle(tmp,(c2-w2,c1-w2),(c2+w2,c1+w2),(0,255,0),1)
    cv2.imshow('Camera', tmp)
    if( (31<H<83) and (34<S<127) and (66<V<206)):
        print("piece is green")
        R1='green'
        print(R1)
    elif( (0<H<40) and (41<S<120) and (183<V<255)):
        print("piece is yellow")
        R1='yellow'
        print(R1)
    elif((0<H<20) and (128<S<255) and (139<V<255)):
        print("piece is red")
        R1='red'
        print(R1)
    else:
        print("don't know")
        i=0
    i=i+1
    if (((R1=='green') or (R1=='yellow') or (R1=='red')) and (i>=10)):
       print("new game piece")
       i=0
       break
    # Stop program if q is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

while(cv2.getWindowProperty("Camera", 0) >= 0):
    # Read Image
    _, img = capture.read()
    # Resize image
    tmp = cv2.resize(img, output_res)
    # Convert from BGR to HSV
    hsv = cv2.cvtColor(tmp, cv2.COLOR_BGR2HSV)
    hue=hsv[:,:,0]
    sat=hsv[:,:,1]
    val=hsv[:,:,2]
    # Threshold for the brightest objects, optional
    # Adjust if you want to threshold for your game piece
    thresholded = cv2.inRange(hsv, (0,0,254),(255,255,255) )
    ####
    # Show area of interest
    # Calculate average intensity, saturation and hue in ROI
    c1=100
    c2=150
    w2=35
    ROI=val[c1-w2:c1+w2,c2-w2:c2+w2]
    V=np.sum(ROI, dtype=np.uint32)/(2*w2+1)/(2*w2+1)
    ROI=sat[c1-w2:c1+w2,c2-w2:c2+w2]
    S=np.sum(ROI, dtype=np.uint32)/(2*w2+1)/(2*w2+1)
    ROI=hue[c1-w2:c1+w2,c2-w2:c2+w2]
    H=np.sum(ROI, dtype=np.uint32)/(2*w2+1)/(2*w2+1)
    tmp = cv2.putText(tmp, f"H:{H:3.1f} S:{S:3.1f} V:{V:3.1f}" , (c2-w2, c1+3*w2), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1, cv2.LINE_AA)
    cv2.rectangle(tmp,(c2-w2,c1-w2),(c2+w2,c1+w2),(0,255,0),1)
    cv2.imshow('Camera', tmp)
    if( (31<H<83) and (34<S<127) and (66<V<206)):
        print("piece is green")
        R2='green'
        print(R2)
    elif( (0<H<40) and (41<S<120) and (183<V<255)):
        print("piece is yellow")
        R2='yellow'
        print(R2)
    elif( (0<H<20) and (128<S<255) and (139<V<255)):
        print("piece is red")
        R2='red'
        print(R2)
    else:
        print("don't know")
        i=0
    i=i+1
    if ((R1!=R2) and((R2=='green') or (R2=='yellow') or (R2=='red')) and (i>=10)):
      print("new game piece")
      break
    # Stop program if q is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

if ((R1=='green' and R2=='red') or (R1=='red' and R2=='green')):
    print("piece is yellow")
    R3='yellow'
if ((R1=='green' and R2=='yellow') or (R1=='yellow' and R2=='green')):
    print("piece is red")
    R3='red'
if ((R1=='yellow' and R2=='red') or (R1=='red' and R2=='yellow')):
    print("piece is green")
    R3='green'

print("finished")
print(R1)
print(R2)
print(R3)
cv2.destroyAllWindows()

######################
#end of camera use
######################
#insert desired order
######################

S1=''
S2=''
T1=''
T2=''
T3=''
T1=str(input("Enter in target bottom piece: "))
T2=str(input("Enter in target middle piece: "))
T3=str(input("Enter in target top piece: "))
print(T1)
print(T2)
print(T3)

###############
#start of meArm
###############

arm = meArm.meArm()
arm.begin(0,0x60) # block address of motor controller
arm.gotoPoint(   0, 150,   50)

if(R3==T1):
    #grab top piece in repository and move it to Target
    if(R2==T2):
        #grab middle piece in repository and move it to stack Target
        #grab bottom piece in repository and move it to top stack Target
        #end of game
        print("end game")
    else:
        #move middle piece in repository to staging
        #move bottom piece in repository to stack target
            #has to clear bottom piece in staging
        #move bottom piece in staging to top target
        print("end game")
else:
    #move top piece in repository to staging
    S1=R3
    R3=''
    if(R2==T1):
        #move middle piece in repository to target
        if(R1==T2):
            #move bottom piece in repository to stack on target
                #has to move over bottom piece in staging
            #move bottom piece in staging to stack on target top
            print("end game")
        else:
            #move bottom piece in staging to stack on target
            #move bottom piece in repository to stack on target top
            print("end game")
    else:
        #move middle piece in repository to stack on staging
        S2=R2
        R2=''
        #move bottom piece in repository to target
            #has to move over 2 stacked pieces in staging
        if(S2==T2):
            #move top piece in staging to stack target
            #move bottom piece in staging to stack target top
            print("end game")
        else:
            #move top piece in staging back to bottom repository
            #move bottom piece in staging to stack target
            #move piece in repository to stack target top
            print("end game")