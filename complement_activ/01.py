import cv2
import numpy as np
# capture = cv2.VideoCapture(0)
capture = cv2.VideoCapture("IFMA Campus Caxias.mp4")
logo = cv2.imread('logo-if-vertical.png')

kernel = np.ones((3,3),np.uint)

frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)

logo = cv2.resize(logo,(200,170),interpolation=cv2.INTER_AREA)

if not capture.isOpened():
    print("Erro ao acessar camera")
else:
    while capture.isOpened():
        ret, frame = capture.read()
        
        if ret is True:
           
            roi= frame[35:153,1140:1220]
            gray = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
            ret, mask_inv = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY)
            mask = cv2.bitwise_not(mask_inv)
        
            telea = cv2.inpaint(roi,mask_inv,3,cv2.INPAINT_TELEA)

            frame[35:153,1140:1220] = telea

            cv2.imshow('Input', telea)
            cv2.imshow('region', roi)
            cv2.imshow('final1', frame)

            if cv2.waitKey(20) & 0xFF == ord('q'):
                break

        else: break

capture.release()
cv2.destroyAllWindows()
