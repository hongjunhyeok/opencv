import cv2
import numpy as np
FILENAME="empty"
PATH="videos/vari/video1.avi"
SAVEPATH="empty_veri1/"
cap=cv2.VideoCapture(PATH)
ret,frames=cap.read()
count=3000
while ret:
    count+=1
    _, frames = cap.read()
    if(count%1==0):
        gray=cv2.cvtColor(frames,cv2.COLOR_BGR2GRAY)
        frames=gray[170:550,420:900]

        cv2.imwrite(SAVEPATH+FILENAME+"_%05d.jpeg"%count,frames)
    if cv2.waitKey(1)&0xFF==27:
        break

cap.release()