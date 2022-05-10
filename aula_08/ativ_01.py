# coding=utf-8
import cv2

img = cv2.imread('noise.jpg')

ksize=7

median = cv2.medianBlur(img,ksize)

cv2.imshow('Img',img)
cv2.imshow('Median',median)

cv2.waitKey(0)
cv2.destroyAllWindows()
