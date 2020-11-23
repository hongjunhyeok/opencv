import cv2
import os
import random
import time
import numpy as np




IMGPATH="filled/"

scaleFactor=1.1
minNeighbors=2

CROP_W=20
CROP_H=40
_FRAME_COUNT=100

MODE_IMAGE_PROCESS=1
MODE_VIDEO_PROCESS=2
mode = MODE_VIDEO_PROCESS

count=0

def doProcess(mode):


    curTime=time.time();
    FLAG_ENTER = True
    FLAG_EMPTY = True
    FLAG_FILLED =True
    FLAG_LEAVE = True
    FLAG_TIMER=True

    # VIDIOPATH ="videos/videoz.avi"
    FILEPATH="img/0_result/"

    # CASCADEPATH1="cascades/filled4020_n.xml"


    CASCADEPATH1="cascades/empty10802.xml" #circle.xml"
    CASCADEPATH2="cascades/filled1080.xml"
    CASCADEPATH3="cascades/filled_200829.xml"
    CASCADEPATH4="cascades/filled_200829.xml"
    CASCADEPATH5="cascades/filled_200829.xml"

    cascade1=cv2.CascadeClassifier(CASCADEPATH1)
    cascade2=cv2.CascadeClassifier(CASCADEPATH2)
    cascade3=cv2.CascadeClassifier(CASCADEPATH3)
    cascade4=cv2.CascadeClassifier(CASCADEPATH4)
    cascade5=cv2.CascadeClassifier(CASCADEPATH5)

    isOk=False
    enterMN=15
    count=0
    acount=0
    framecount=0;
    positiveCount=0;
    NegativeCount=0;
    th=0;
    # ret, frame = cap.read()
    #조건 1.1 10

    # print("START")
    # random.seed(4233334)
    # filedir=os.listdir(IMGPATH)
    # for file in random.sample(range(1000,7420),400):



    minNeighborList=[3]
    if mode== MODE_IMAGE_PROCESS:


            for file in filedir:


                img=cv2.imread(IMGPATH+str(file))
                img=img[0:400,75:475]
                cv2.imwrite(str(file),img)


            print(str((minNeighbors))+" : Total : {0}, Positive {1}, Negative {2}".format(count, positiveCount, NegativeCount))
            count=0
            positiveCount=0
            NegativeCount=0





    if mode == MODE_VIDEO_PROCESS:

        prevTime=0
        cap=cv2.VideoCapture("videos/empty1080.mp4")
        ret=True

        while ret:

            curTime=time.time()
            sec=curTime-prevTime
            prevTime=curTime

            fps=1/sec
            print("fps: %.f"%fps)

            ret, frame = cap.read()
            frame=np.array(frame)
            framecount+=1

            crop_img = frame[500:1000,0:500]



            enter=cascade1.detectMultiScale(crop_img,1.1,1)#350
            filled=cascade2.detectMultiScale(crop_img,1.1,200)#190?
            leave=cascade3.detectMultiScale(crop_img,1.1,300)#300
            empty = cascade4.detectMultiScale(crop_img, 1.1,160) #160~
            bubble = cascade5.detectMultiScale(crop_img,1.1,2,minSize=(14,14))

            if FLAG_ENTER:
                for(x,y,w,h) in enter:
                    acount+=1
                    dccount=0
                    cv2.rectangle(crop_img, (x ,y), (x + w , y + h), (255, 255, 255), 2)
                    cv2.putText(crop_img, "Fluid empty", (10,100), 2, 2, (255, 255, 255), 2)



            if FLAG_FILLED:
                for (x, y, w, h) in filled:
                    acount += 1
                    dccount = 0
                    cv2.rectangle(crop_img, (x, y), (x + w, y + h), (255, 0, 255), 2)
                    cv2.putText(crop_img,"Fluid Filled",(10,100),2,2,(255,0,255),2)

            # if FLAG_LEAVE:
            if framecount>1:
                cv2.imshow("cc1",crop_img)
            # cv2.imshow("cc2", crop_img / saveimg)
            # print(img3)

            if cv2.waitKey(1) & 0xFF == 27:
                break


        cap.release()
        cv2.destroyAllWindows()
doProcess(MODE_VIDEO_PROCESS)
