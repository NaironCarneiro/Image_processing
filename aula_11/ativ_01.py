import cv2
import numpy as np

kernel = np.ones((5,5),np.uint)

img = cv2.imread('morphological_car.png')

black_hat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
top_hat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)


img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('img original', img)
cv2.imshow('black', black_hat)
cv2.imshow('top hat', top_hat)

cv2.waitKey(0)
cv2.destroyAllWindows()
