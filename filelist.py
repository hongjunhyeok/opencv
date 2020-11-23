import os
import cv2





img =cv2.imread("colorband.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

b=img.shape[0]
a=img.shape[1]
resized=cv2.resize(img,(int((a/8)),int((b/8))))


cv2.imshow("r",resized)
cv2.imwrite("col8.jpg",resized)
q=cv2.waitKey(1)
if q==27:
    cv2.destroyAllWindows()

