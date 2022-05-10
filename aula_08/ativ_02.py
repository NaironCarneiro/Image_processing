import cv2
import numpy as np

img = cv2.imread("cars.png")
color =  (255,255,255)
mask = np.ones(img.shape, np.uint8)

cv2.circle(mask, (mask.shape[1] - 480, mask.shape[0] - 300), 260, color,-1)

mask = cv2.GaussianBlur(mask, (51, 51), 51)

reverseMask = cv2.bitwise_not(mask)
imgBlur = cv2.blur(img, (50,50))

imgMaskedBack = imgBlur * (reverseMask / 255)
imgMaskedBack = imgMaskedBack.astype(np.uint8)

imgMaskedfocus = img * (mask / 255)
imgMaskedfocus = imgMaskedfocus.astype(np.uint8)

output = imgMaskedBack + imgMaskedfocus

cv2.imshow('Img', img)
cv2.imshow('output', output)

cv2.waitKey(0)
cv2.destroyAllWindows()