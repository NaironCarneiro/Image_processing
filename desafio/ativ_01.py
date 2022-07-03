import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier('classifiers/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('classifiers/haarcascade_eye.xml')
mouth_cascade = cv2.CascadeClassifier('classifiers/haarcascade_mcs_mouth.xml')

cap = cv2.VideoCapture("IFMA Campus Caxias.mp4")
sungalsses = cv2.imread('sungalsses.png', cv2.IMREAD_UNCHANGED)
moustache = cv2.imread('moustache.png', cv2.IMREAD_UNCHANGED)

def resizeEyes(image):
    image = cv2.resize(image, ((150),(26)), interpolation=cv2.INTER_AREA)
    return image

def resizeMoustache(image):
    image = cv2.resize(image, ((100),(26)), interpolation=cv2.INTER_AREA)
    return image

def filtro(image, objeto, x, y, w, h):
    rows, cols = objeto.shape[:2]
    alpha = objeto[:, :, 3] / 255
    overlay = objeto[:, :, :3]
    mask = np.dstack((alpha, alpha, alpha))
    roi = image[(y-h):(y-h) + rows, (x-w):(x-w) + cols]
    output = roi * (1 - mask) + overlay * mask
    image[(y-h):(y-h) + rows, (x-w):(x-w) + cols] = output
    return image


while True:
    ret, frame = cap.read()
    if ret is True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,scaleFactor=1.2, minNeighbors=15,  minSize=(20, 20))
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            ponto1,ponto2 = ((x+(x+w))/2),((y+(y+h))/2)
            center1 = (int(ponto1)+int(ponto2))/2
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:(y+h+200), x:(x+w+200)]
            eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.3, minNeighbors=10,  minSize=(20, 20))
            print("coordenadas faces",int(center1),int(ponto1))
            cv2.circle(roi_color, (int(center1),int(ponto1)), 30,(255,0,0))
            for (ex,ey,ew,eh) in eyes:
                # cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                roi_color = filtro(roi_color, resizeEyes(sungalsses),int(ew+10),int(eh+60), 20, 20)
                mouth = mouth_cascade.detectMultiScale(roi_gray, scaleFactor=2.0, minNeighbors=20,  minSize=(20, 20))
                for (mx, my, mw, mh) in mouth:
                    # cv2.rectangle(roi_color,(mx,my),(mx+mw,my+mh),(0,0,255),2)
                    roi_color = filtro(roi_color, resizeMoustache(moustache),int(mw-10),int(mh+100), 20, 20)
        cv2.imshow('Video IFMA', frame)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    else: break

cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()