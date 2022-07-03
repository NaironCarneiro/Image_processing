# import cv2
# import numpy as np
# face_cascade = cv2.CascadeClassifier('classifiers/haarcascade_frontalface_default.xml')
# # eye_cascade = cv2.CascadeClassifier('classificadores/haarcascade_eye.xml')
# face = []
# count = 0
# capture = cv2.VideoCapture("videoG1.mp4")
# if not capture.isOpened():
#     print("Erro ao acessar camera")
# else:
#     while capture.isOpened():
#         ret, frame = capture.read()
#         if ret is True:
#             frame = cv2.resize(frame,(620,380),interpolation=cv2.INTER_AREA)
#             gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
             
#             faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=15,  minSize=(20, 20))
#             if len(faces) != 0:
#                 face.append(len(faces))
#                 count = len(faces) + 1
#                 for (x,y,w,h) in faces:
#                     cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

#             text = "{} faces".format(len(faces))
#             cv2.putText(frame, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
#                 0.5, (0, 255, 0), 2)
#             cv2.imshow('Original', frame)
#             print('total de faces encontradas: ', count)
            
#             if cv2.waitKey(20) & 0xFF == ord('q'):
#                 break
    
#         else: break
#     # cont = len(faces) +1
    

# capture.release()
# cv2.destroyAllWindows()


import cv2
import numpy as np

oculos = cv2.imread('sungalsses.png', cv2.IMREAD_UNCHANGED)
bigode = cv2.imread('moustache.png', cv2.IMREAD_UNCHANGED)


face_cascade = cv2.CascadeClassifier('classifiers/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('classifiers/haarcascade_eye.xml')
mouth_cascade = cv2.CascadeClassifier('classifiers/haarcascade_mcs_mouth.xml')

porcentagem = 10
def resize(image, width, height):
    width = int(width * porcentagem / 100)
    height = int(height * porcentagem / 100)
    dimensao = (width, height)
    image = cv2.resize(image, dimensao, interpolation=cv2.INTER_AREA)
    return image

# oculos = resize(oculos, porcentagem)
# bigode = resize(bigode, porcentagem)

def filtro(image, objeto, x, y, w, h):
    rows, cols = objeto.shape[:2]
    alpha = objeto[:, :, 3] / 255
    overlay = objeto[:, :, :3]
    mask = np.dstack((alpha, alpha, alpha))
    roi = image[(y-h):(y-h) + rows, (x-w):(x-w) + cols]
    output = roi * (1 - mask) + overlay * mask
    image[(y-h):(y-h) + rows, (x-w):(x-w) + cols] = output
    return image

# face_cascade = cv2.CascadeClassifier('classifiers/haarcascade_frontalface_default.xml')
# profile_cascade = cv2.CascadeClassifier('classifiers/haarcascade_profileface.xml')

video = cv2.VideoCapture("IFMA Campus Caxias.mp4")
# video.set(cv2.CAP_PROP_FPS, 2) 
contfaces = 0
if not video.isOpened():
    print("Erro ao acessar video")
else:   
    while video.isOpened():
        ret, frame = video.read()
        # frame = cv2.resize(frame, resize(frame,1020,880), interpolation=cv2.INTER_AREA)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray)
        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 15)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                roi_color = filtro(roi_color, resize(oculos, ew, eh), ex, ey, 14, -10)
                # break
            mouth = mouth_cascade.detectMultiScale(roi_gray, 2.0, 20)
            for (mx, my, mw, mh) in mouth:
                cv2.rectangle(roi_color,(mx,my),(mx+mw,my+mh),(0,0,255),2)
                roi_color = filtro(roi_color, resize(bigode, mw, mh), mx, my, 15, 30)

        # if (len(faces) and len(profile) > 0):
        #     contfaces += 1

        # text = "{} pessoas".format(contfaces)
        # cv2.putText(frame, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
        #     0.5, (0, 0, 255), 2)

        cv2.imshow('img',frame)
    
        if ret is True:

            key = cv2.waitKey(1)
            if(key == 27):
                break

        else: break

video.release()
cv2.destroyAllWindows()

