# function to take many photos in a row - useful for collecting data for object detection

import numpy as np
import cv2

# define how many photos you want taken
n_photos = 3

#create video capture object
cap = cv2.VideoCapture(0) # 0 is device index

for i in range(n_photos):
	while(True):
		# capture frame by frame
		ret, frame = cap.read()

		# display resulting frame
		cv2.imshow('frame', frame)
		
		k = cv2.waitKey(1) & 0xFF
		if k == ord('s'):
			file_path = 'image_data/saved_image_' + str(i) + '.png'
			cv2.imwrite(file_path, frame)
			break
		if k == 27: # if press escape
			break

# release capture object
cap.release()
cv2.destroyAllWindows()