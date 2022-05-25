import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('aula11_img.png',0)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((109,109),np.uint)
kernel1 = np.ones((109,19),np.uint)
kernelRound = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (121,209))
kernelRound1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (119,119))

# Primeiro exemplo
erosion = cv2.erode(img,kernel,iterations = 1, anchor=(100,100))

# Segundo exemplo
roundedErode1 = cv2.morphologyEx(img, cv2.MORPH_ERODE,kernelRound)
roundedErode2 = cv2.morphologyEx(roundedErode1, cv2.MORPH_ERODE, kernelRound)
roundedDilate = cv2.morphologyEx(roundedErode2, cv2.MORPH_DILATE,kernel1)
roundedFinal = cv2.morphologyEx(roundedDilate, cv2.MORPH_DILATE, kernelRound)

# Terceiro exemplo
roundedDilate = cv2.morphologyEx(img, cv2.MORPH_DILATE, kernelRound1, iterations=2)
roundedErodeFinal = cv2.morphologyEx(roundedDilate, cv2.MORPH_ERODE,kernelRound1)

plt.subplot(221), plt.imshow(img)
plt.title('Imagem')
plt.subplot(222), plt.imshow(erosion)
plt.title('Erosion')
plt.subplot(223), plt.imshow(roundedFinal)
plt.title('border rounded')
plt.subplot(224), plt.imshow(roundedErodeFinal)
plt.title('dilate border')


plt.tight_layout()
plt.show()