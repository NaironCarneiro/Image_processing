import cv2
# capture = cv2.VideoCapture(0)
capture = cv2.VideoCapture("IFMA Campus Caxias.mp4")
logo = cv2.imread('logo-if-vertical.png')

frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
logo = cv2.resize(logo,(200,170),interpolation=cv2.INTER_AREA)
if not capture.isOpened():
    print("Erro ao acessar camera")
else:
    while capture.isOpened():
        ret, frame = capture.read()
        if ret is True:

            gray = cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)
            ret, mask_inv = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)
            mask = cv2.bitwise_not(mask_inv)
            roi= frame[:180,1080:]
            telea = cv2.inpaint(roi,mask,3,cv2.INPAINT_TELEA)

           
            cv2.imshow('Input', frame)
            cv2.imshow('region', roi)
            cv2.imshow('final', mask)

            if cv2.waitKey(20) & 0xFF == ord('q'):
                break

        else: break

capture.release()
cv2.destroyAllWindows()
