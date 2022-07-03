import cv2
import numpy as np
face_cascade = cv2.CascadeClassifier('classifiers/haarcascade_frontalface_default.xml')

count = 0
capture = cv2.VideoCapture("videoG1.mp4")
while True:
	ret, frame = capture.read()
	if ret is True:
		frame = cv2.resize(frame,(620,380),interpolation=cv2.INTER_AREA)
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=15,  minSize=(20, 20))
		f = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
		for (x,y,w,h) in faces:
    		
			cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
			roi_gray = gray[y:y+h, x:x+w]

			count = count+1
				
		text = "{} faces".format(count)
		cv2.putText(frame, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
			0.5, (0, 255, 0), 2)
		cv2.imshow('Original', frame)
		if cv2.waitKey(20) & 0xFF == ord('q'):
			break

	else: break

capture.release()
cv2.destroyAllWindows()