import numpy as np
import cv2

#create video capture object
cap = cv2.VideoCapture(0) # 0 is device index

while(True):
	# capture frame by frame
	ret, frame = cap.read()

	#operations on the frame
	grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# display resulting frame
	cv2.imshow('frame', grey)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# release capture object
cap.release()
cv2.destroyAllWindows()