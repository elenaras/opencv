import numpy as np
import cv2

# load colour image in grayscale
img = cv2.imread('lambeth_bridge.png', 0)

# display image
cv2.imshow('image', img) # first argument is window name, second is image
cv2.waitKey(0) # because 0 is specified, it will wait indefinitely for a key stroke
cv2.destroyAllWindows()

# load colour image in colour
img = cv2.imread('lambeth_bridge.png', 1)

# CREATING WINDOW FIRST:
cv2.namedWindow('image', cv2.WINDOW_NORMAL) # WINDOW_NORMAL flag means we'll be able to resize the image
cv2.imshow('image', img)
# display image for 5 seconds
cv2.waitKey(5000)
cv2.destroyAllWindows()


# ADDING SAVING FUNCTIONALITY
# load in grayscale
img = cv2.imread('lambeth_bridge.png', 0)
cv2.imshow('image', img)
k = cv2.waitKey(0) & 0xFF
if k == 27: # if press 'escape'
	cv2.destroyAllWindows()
if k == ord('s'): # if press 's'
	cv2.imwrite('lambeth_bridge_grey.png', img)
	cv2.destroyAllWindows()


# USING MATPLOTLIB
import matplotlib.pyplot as plt

img = cv2.imread('lambeth_bridge.png', 0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # hiding tick values on x and y axes
plt.show()
# note that matplotlib uses rgb, but opencv uses bgr