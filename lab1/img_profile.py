import cv2 
import numpy as np

img=cv2.imread("wp3013104.jpeg")

size=img.shape
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]
 
address="/Users/apple/Desktop/code/Digital_Image_processing/wp3013104.jpeg"
print('Image Dimension    : ',size)
print('Image Height       : ',height)
print('Image Width        : ',width)
print('Number of Channels : ',channels)
print("Resolution of image is :"+str(width) + "x" + str(height))
print("Image is located at-: "+address)

number_of_white_pix = np.sum(img == 255)
number_of_black_pix = np.sum(img == 0)
  
print('Number of white pixels:', number_of_white_pix)
print('Number of black pixels:', number_of_black_pix)

