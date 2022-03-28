import cv2
import time

zahl = 0

cam = cv2.VideoCapture(0)
for i in range(10000):
    _, frame = cam.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.blur(frame,(15,15))
    frame = cv2.resize(frame,(28,28))
    
    cv2.imshow("",cv2.resize(frame,(400,400)))
    key =  cv2.waitKey(30)
    
    
    if key == ord(" "):
        cv2.imwrite("unsere_daten/"+str(zahl)+"/"+str(zahl)+"_"+str(time.time())+".jpg", frame)
        
    if key == 27:
        break
        
    
    
