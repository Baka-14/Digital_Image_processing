import cv2
import numpy as np
from scipy import ndimage

img = cv2.imread("galaxy.jpeg", 0)
cv2.imshow('Original Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# (1/9 3X3 K matrix) Low Pass Kernel
kernel_1 = np.ones((3,3), np.float32)/9
dst_1 = cv2.filter2D(img,-1, kernel_1)
cv2.imshow('Low pass Filters 1/9  3X3 K Matrix', dst_1)
cv2.waitKey(0)
cv2.destroyAllWindows()

# (1/5 3X3 K matrix) Low Pass Kernel 
kernel_2 = np.ones((3,3), np.float32)/5
dst_2 = cv2.filter2D(img,-1, kernel_2)                                                                                                
cv2.imshow('Low pass Filters 1/5  3X3 K Matrix', dst_2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#(1/1 3X3 MATRIX) Low pass kernel 
kernel_3 = np.ones((3,3), np.float32)/1
dst_3 = cv2.filter2D(img,-1, kernel_3)                                                                       
cv2.imshow('Low pass Filters 1/1 3X3 K Matrix', dst_3)
cv2.waitKey(0)
cv2.destroyAllWindows()

# High Pass kernel (Middle Value 3) 
kernel_3x3 = np.array(
[[-1, -1, -1],
[-1, 3, -1],
[-1, -1, -1]]) 
k3 = ndimage.convolve(img, kernel_3x3)
cv2.imshow('Original Image', img)
cv2.imshow('hpf 3', k3)
cv2.waitKey(0)
cv2.destroyAllWindows() 

# High Pass Kernel (Middle Value 5)
kernel_5 = np.array(
[[-1, -1, -1],
[-1, 5, -1],
[-1, -1, -1]])
k5 = ndimage.convolve(img, kernel_5)
cv2.imshow('Original Image', img)
cv2.imshow('hpf 5', k5)
cv2.waitKey(0)
cv2.destroyAllWindows()

# High Pass Kernel (Middle Value 9)

kernel_9 = np.array(
[[-1, -1, -1],
[-1, 9, -1],
[-1, -1, -1]])
k9 = ndimage.convolve(img, kernel_9)
cv2.imshow('Original Image', img)
cv2.imshow('hpf 9', k9)
cv2.waitKey(0)
cv2.destroyAllWindows() 

