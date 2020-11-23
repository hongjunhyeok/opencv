import cv2
import numpy as np
from scipy.signal import correlate
img=cv2.imread('before.jpg')
img2=cv2.imread('after.jpg')

# print(img2.shape())
# img3=cv2.imwrite("sss",(255,255,255))
img=np.array(img)
w=img.shape[0]
h=img.shape[1]
print(w,h)

img3=np.zeros((w,h,3)).reshape((w,h,3))

img4=np.zeros((180,200,3)).reshape((180,200,3))
img4[:,:,0:3]=2

img=np.array(img)
img2=np.array(img2)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if (img2[i,j,2]/img[i,j,2] >= 0.95):
            img3[i,j]=img2[i,j]/img[i,j]
        else:
            img3[i,j]=(0.9,0.9,0.9)

img4=img2

print(img3[55,65])
cv2.imshow('b',img)
cv2.imshow('a',img2)
cv2.imshow('img3',img3)

q=cv2.waitKey(0)
if (q == 27):
    cv2.destroyAllWindows()