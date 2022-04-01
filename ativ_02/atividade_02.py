import cv2
import numpy as np

img = cv2.imread('logo-if.jpg')

cv2.imshow('original', img)

(height, width) = img.shape[0:2]
low_img = np.zeros(img.shape, np.uint8)

def func_matrix(m):
    return cv2.mean(m)[:3]

for i in range(width):
    for j in range(height):
        matrix = img[j-1:j+2, i-1: i+2]
        low_img[j, i] = func_matrix(matrix)

cv2.imshow('imagem menor', low_img)
 
cv2.waitKey(0)
cv2.destroyAllWindows()