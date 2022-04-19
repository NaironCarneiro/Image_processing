# coding=utf-8
import cv2
import numpy as np

img = cv2.imread('logo-if.jpg')

rows,cols = img.shape[:2]

M = np.float32([[1,0,100],[0,1,50]])
M = cv2.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
res = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img',img)
cv2.imshow('res',res)

cv2.waitKey(0)
cv2.destroyAllWindows()