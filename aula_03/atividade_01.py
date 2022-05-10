from multiprocessing.dummy import Event
from random import randint
import cv2

BLUE = (255, 0, 0)
GREEN = (0, 255, 0)
RED = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)

COLORS=[BLUE,GREEN,RED,BLACK,GRAY]
c = 2
def draw_circle(event,x,y,flags,param):
    global drawing
    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        circles.append((x,y))

    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing==True:
            circles.append((x,y))

    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False
        circles.append((x,y))

capture = cv2.VideoCapture("batman-trailer-3.mp4")

cv2.namedWindow('batman')
cv2.setMouseCallback('batman',draw_circle)

frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv2.CAP_PROP_FPS)
circles = []
if not capture.isOpened():

    print("Erro ao reproduzir video")
else:
    fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
    output = cv2.VideoWriter("video-rabiscado.avi", fourcc, int(fps), (int(frame_width), int(frame_height)), True)
    while capture.isOpened():        
        ret, frame = capture.read()
        if ret is True:     
            # fazer circulos se tornando rabiscos no video    
            for center_position in circles:
                cv2.circle(frame, center_position,3,COLORS[c],-1)

            output.write(frame)

            cv2.imshow('batman',frame)

            key = cv2.waitKey(30) & 0xff
            if key == 27:
                break

            # Apagar todos os rascunhos
            elif key == 32:
                circles = []
            
            # mudar a cor do rabisco
            if key == 99:
                c=randint(0,len(COLORS)-1)


capture.release()
output.release()
cv2.destroyAllWindows()