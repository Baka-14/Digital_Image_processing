import cv2;
import numpy as np;
import matplotlib.pyplot as plt

im_in = cv2.imread("/Users/apple/Desktop/code/Digital_Image_processing/coins.jpeg", cv2.IMREAD_GRAYSCALE)
th, im_th = cv2.threshold(im_in, 220, 255, cv2.THRESH_BINARY_INV)
im_floodfill = im_th.copy()
h, w = im_th.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)

cv2.floodFill(im_floodfill, mask, (0,0), 255)
im_floodfill_inv = cv2.bitwise_not(im_floodfill)
im_out = im_th | im_floodfill_inv

plt.imshow(im_in)                                                                                                                                                                                                                                                                                                                                                                                
plt.title('Original Image')                               
plt.show()
plt.imshow(im_floodfill)
plt.title('Floodfilled Image')
plt.show()
plt.imshow(im_floodfill_inv)
plt.title('Inverted Floodfilled Image')
plt.show()
plt.imshow(im_out)
plt.title('Foreground')
plt.show()

