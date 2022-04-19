#coding=utf-8
import cv2

img_logo = cv2.imread('logo-if.jpg')
img_ifma = cv2.imread('ifma-caxias.jpg')

#Redimensiona imagem
img_logo = cv2.resize(img_logo,(160,80),interpolation=cv2.INTER_AREA)

rows, cols, channels = img_logo.shape
region_interest = img_ifma[0:rows, 0:cols]

gray = cv2.cvtColor(img_logo,cv2.COLOR_BGR2GRAY)
ret, mask_inv = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)
mask = cv2.bitwise_not(mask_inv)

img_ifma1 = cv2.bitwise_and(region_interest,region_interest,mask=mask_inv)
img_logo1 = cv2.bitwise_and(img_logo,img_logo, mask=mask)

final_logo = cv2.add(img_logo1,img_ifma1)
img_ifma[0:rows, 0:cols ] = final_logo

# cv2.imshow('Original',img_logo)
# cv2.imshow('Grayscale',gray)
# cv2.imshow('Threshold',mask)
# cv2.imshow('Mask Inv',mask_inv)
# cv2.imshow('dst',final_logo)
cv2.imshow('final',img_ifma)
cv2.waitKey(0)
cv2.destroyAllWindows()