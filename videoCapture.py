import cv2


capture= cv2.VideoCapture("videos/newPillar_1.mp4")

width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
writer = cv2.VideoWriter('output2.avi', fourcc, 60.0, (600,500))


record = False
count=1000
while True:


    count+=1
    if count < 1500:
        continue
    ret,frame=capture.read()
    # crop_img = frame
    crop_img = frame[200:700, 700:1300]

    if ret==False:
        break


    if count>3000:
        break

    cv2.imshow("C",crop_img)

    writer.write(crop_img)


    if cv2.waitKey(1)&0xFF==27:
        break


capture.release()
writer.release()
cv2.destroyAllWindows()