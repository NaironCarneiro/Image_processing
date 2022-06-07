import re
import cv2
# capture = cv2.VideoCapture(0)

def aspecRatioVideo(resize):
    resize = cv2.resize(resize, (720, 480), interpolation = cv2.INTER_LINEAR)
    return resize

def cropVideo(crop):
    crop = crop[0:480, 0:720]
    return crop

capture = cv2.VideoCapture("IFMA Campus Caxias.mp4")

frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
print('width :',frame_width)
print('height :',frame_height)
cont = 1
if not capture.isOpened():
    print("Erro ao acessar camera")
else:
       
    while capture.isOpened():
        ret, frame = capture.read()
                # padrão (1280 x 720) = 16:9
                # (720 x 480) = 4:3
        if ret is True:

            if (cv2.waitKey(20) & 0xFF == ord('a')):
                frame = aspecRatioVideo(frame)
            elif (cv2.waitKey(20) & 0xFF == ord('c')):
                frame = cropVideo(frame)

            cv2.imshow('Input', frame)

            if (cv2.waitKey(20) & 0xFF == ord('c')):
                crop = frame[0:480, 0:720]
               
                

            if cv2.waitKey(20) & 0xFF == ord('q'):
                break

        else: break



capture.release()
cv2.destroyAllWindows()
