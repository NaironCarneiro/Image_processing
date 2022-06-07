import cv2
# Dimensões do video
# padrão (1280 x 720) = 16:9
# (720 x 480) = 4:3

def aspecRatioVideo(resize):
    resize = cv2.resize(resize, (720, 480), interpolation = cv2.INTER_LINEAR)
    return resize

def cropVideo(crop):
    crop = crop[0:480, 0:720]
    return crop

press_a = False
press_c = False
capture = cv2.VideoCapture("IFMA Campus Caxias.mp4")

if not capture.isOpened():
    print("Erro ao acessar camera")
else:
       
    while capture.isOpened():
        ret, frame = capture.read()

        if ret is True:

            if (cv2.waitKey(20) & 0xFF == ord('a')):
                press_a = True
                
            elif (cv2.waitKey(20) & 0xFF == ord('c')):
                press_c = True

            if press_a is True:
                frame = aspecRatioVideo(frame)
                cv2.imshow('Input', frame)
                if (cv2.waitKey(20) & 0xFF == ord('a')):
                    press_a = False

            if press_c is True:
                frame = cropVideo(frame)
                cv2.imshow('Input', frame)
                if (cv2.waitKey(20) & 0xFF == ord('c')):
                    press_c = False


            cv2.imshow('Input', frame)

            key = cv2.waitKey(30) & 0xff
            if key == 27:
                break

        else: break



capture.release()
cv2.destroyAllWindows()
