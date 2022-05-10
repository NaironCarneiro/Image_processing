import cv2
import numpy as np

img = cv2.imread('logo-if.jpg')

cv2.imshow('original', img)

(height, width) = img.shape[0:2]

low_width = int(width/3)
low_height = int(height/3)
low_img = np.zeros((low_height, low_width,3), np.uint8)

def func_matrix(m):
    return m[1, 1]

for i in range(low_width):
    initial_i = i*3
    for j in range(low_height):
        initial_j = j*3
        matrix = img[initial_j: initial_j+3, initial_i: initial_i+3]
        low_img[j, i] = func_matrix(matrix)

cv2.imshow('imagem menor', low_img)
 
cv2.waitKey(0)
cv2.destroyAllWindows()