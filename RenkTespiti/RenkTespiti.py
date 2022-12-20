#Görüntü Üzerinde Renk Tespiti

import cv2
import numpy as np

image=cv2.imread('trafiklambasi.jpeg')
genislik=650
yukseklik=360
image=cv2.resize(image, (genislik,yukseklik))

hsv_image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

low_yellow=np.array([20, 120, 80])
high_yellow=np.array( [45, 200, 255])


mask= cv2.inRange(hsv_image, low_yellow, high_yellow)
mask= cv2.erode(mask,None,iterations=2)
mask=cv2.dilate(mask,None,iterations=2)
mask=cv2.GaussianBlur(mask,(3,3),0)
cnts=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]


#Zehra add pull request 

low_red=np.array([170,50,70])
high_red=np.array([180,255,255])

mask= cv2.inRange(hsv_image, low_red, high_red)
mask= cv2.erode(mask,None,iterations=2)
mask=cv2.dilate(mask,None,iterations=2)
mask=cv2.GaussianBlur(mask,(3,3),0)
cnts=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]


for cnt in cnts:
    (x , y , w , h) = cv2.boundingRect(cnt)
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),4)

cv2.imshow("Sonuc",image)
cv2.waitKey(0)
cv2.destroyAllWindows()


