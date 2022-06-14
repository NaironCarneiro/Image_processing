# coding=utf-8
import cv2
import numpy as np
import math

img = cv2.imread('coins.jpeg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (7, 7),cv2.BORDER_DEFAULT)

_,process = cv2.threshold(blur,220,255,cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(process, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0,255,0), 2)

for cnt in contours:
    M = cv2.moments(cnt)
    if M['m00'] != 0:
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv2.circle(img,(cx,cy),3,(255,0,0),-1)

    area = cv2.contourArea(cnt)
    perimeter = cv2.arcLength(cnt,True)
    diametro = int(perimeter/math.pi)
    print("Area: ", area, "Perimetro: ",perimeter, "Diametro: ",diametro)

    if(diametro == 186 ):
        cv2.putText(img, "1 real", (cx - 30, cy - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    if(diametro == 158 ):
        cv2.putText(img, "50 centavos", (cx - 50, cy - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    if(diametro == 168 ):
        cv2.putText(img, "25 centavos", (cx - 50, cy - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    if(diametro == 146):
        cv2.putText(img, "5 centavos", (cx - 50, cy - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    if(diametro == 132):
        cv2.putText(img, "10 centavos", (cx - 50, cy - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

    x,y,w,h = cv2.boundingRect(cnt)
    # cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

    (x,y),radius = cv2.minEnclosingCircle(cnt)
    center = (int(x),int(y))
    radius = int(radius)
    cv2.circle(img,center,radius,(0,255,0),2)

    

cv2.imshow('Contours',img)

cv2.waitKey(0)
cv2.destroyAllWindows()