import cv2
import numpy as np

capture = cv2.VideoCapture("IFMA Campus Caxias.mp4")

kernel = np.ones((3,3),np.uint)

frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)

if not capture.isOpened():
    print("Erro ao acessar camera")
else:
    while capture.isOpened():
        ret, frame = capture.read()
        
        if ret is True:
            canny = cv2.Canny(frame,100,200)
            canny = cv2.cvtColor(canny, cv2.COLOR_BGR2RGB)

            cv2.imshow('Original', frame)
            cv2.imshow('Canny', canny)

            if cv2.waitKey(20) & 0xFF == ord('q'):
                break

        else: break

capture.release()
cv2.destroyAllWindows()
