from re import A
import cv2
import numpy as np
import random
# capture = cv2.VideoCapture(0)
capture = cv2.VideoCapture("batman-trailer-3.mp4")

def increase():
    global a
    a += 0.002

def decrease():
    global a
    a -= 0.002

def noise(image,prob):
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

a = 0

if not capture.isOpened():
    print("Erro ao acessar camera")
else:
    while capture.isOpened():
        ret, frame = capture.read()
        
        if ret is True:

            gray = noise(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY),a)
            
            cv2.imshow('Cinza', gray)

            k = cv2.waitKey(20) & 0xFF
            
            if k == 27:
                break

            if k == ord("a"):
                increase()

            if k == ord("s"):
                decrease()
        else: break

capture.release()
cv2.destroyAllWindows()