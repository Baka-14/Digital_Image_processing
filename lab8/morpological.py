import cv2
import numpy as np

img = cv2.imread('fingerprint.jpeg', 0)

# Taking a matrix of size 5 as the kernel
kernel = np.ones((5, 5), np.uint8)
img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img, kernel, iterations=1)

cv2.imshow('Input', img)
cv2.waitKey(0) 
cv2.destroyAllWindows()
cv2.imshow('Erosion', img_erosion) 
cv2.waitKey(0) 
cv2.destroyAllWindows()
cv2.imshow('Dilation', img_dilation) 
cv2.waitKey(0) 
cv2.destroyAllWindows()

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow('Opening', opening) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel) 
cv2.imshow('Closing', closing) 
cv2.waitKey(0) 
cv2.destroyAllWindows()