# coding=utf-8
import cv2
import numpy as np

img = cv2.imread('logo-if.jpg')
rows,cols = img.shape[:2]

a, b = ((cols-1)/2.0), ((rows-1)/2.0)
def mouse_click(event,x,y,flags,param):
    global a,b
    if event == cv2.EVENT_LBUTTONDOWN:
      a, b = x,y


angle = 0
cv2.namedWindow('Logo IF')
cv2.setMouseCallback('Logo IF',mouse_click)

while(1):
    M = np.float32([[1,0,100],[0,1,50]])
    M = cv2.getRotationMatrix2D((a,b),angle,1)
    res = cv2.warpAffine(img,M,(cols,rows))
    print("point",a,b)
    cv2.imshow('Logo IF',res)

    if cv2.waitKey(20) & 0xFF == ord('r'):
        angle -= 5
        print("ângulo", angle)
      
    if cv2.waitKey(20) & 0xFF == ord('a'):
        angle = 0

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()