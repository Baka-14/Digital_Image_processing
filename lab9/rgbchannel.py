
import numpy as np
import cv2

img = cv2.imread('parrot.webp')
cv2.imshow('Original Image', img)
cv2.waitKey(0)
#g i.e green parts 
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower = np.array([40, 0, 55])
upper = np.array([100, 255, 255])
mask = cv2.inRange(hsv, lower, upper)
result = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('result', result)
cv2.waitKey(0) 

image = result.copy()
new_image = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Gray image', gray)  
cv2.waitKey(0) 
cv2.destroyAllWindows() 
 
# Convert the grayscale image to binary
ret, binary = cv2.threshold(gray, 100, 255,  cv2.THRESH_OTSU) 
cv2.imshow('Binary image', binary)
cv2.waitKey(0) 
cv2.destroyAllWindows() 
 
# To detect object contours, we want a black background and a white 
# foreground, so we invert the image (i.e. 255 - pixel value)
inverted_binary = ~binary
cv2.imshow('Inverted binary image', inverted_binary)
cv2.waitKey(0) 
cv2.destroyAllWindows() 
 
# Find the contours on the inverted binary image, and store them in a list
# Contours are drawn around white blobs.
# hierarchy variable contains info on the relationship between the contours
contours, hierarchy = cv2.findContours(inverted_binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
       
# Draw the contours (in red) on the original image and display the result
# Input color code is in BGR (blue, green, red) format
# -1 means to draw all contours
with_contours = cv2.drawContours(image, contours, -1,(255,0,255),3)
cv2.imshow('Detected contours', with_contours)
cv2.waitKey(0)
cv2.destroyAllWindows() 

#for b i.e blue 
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower = np.array([110,50,50])
upper= np.array([130,255,255])
mask = cv2.inRange(hsv, lower, upper)
result = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('result', result)
cv2.waitKey(0) 

image = result.copy()
new_image = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Gray image', gray)  
cv2.waitKey(0) 
cv2.destroyAllWindows() 
 
# Convert the grayscale image to binary
ret, binary = cv2.threshold(gray, 100, 255,  cv2.THRESH_OTSU) 
cv2.imshow('Binary image', binary)
cv2.waitKey(0) 
cv2.destroyAllWindows() 
 
# To detect object contours, we want a black background and a white 
# foreground, so we invert the image (i.e. 255 - pixel value)
inverted_binary = ~binary
cv2.imshow('Inverted binary image', inverted_binary)
cv2.waitKey(0) 
cv2.destroyAllWindows() 
 
# Find the contours on the inverted binary image, and store them in a list
# Contours are drawn around white blobs.
# hierarchy variable contains info on the relationship between the contours
contours, hierarchy = cv2.findContours(inverted_binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
       
# Draw the contours (in red) on the original image and display the result
# Input color code is in BGR (blue, green, red) format
# -1 means to draw all contours
with_contours = cv2.drawContours(image, contours, -1,(255,0,255),3)
cv2.imshow('Detected contours', with_contours)
cv2.waitKey(0)
cv2.destroyAllWindows() 

image = result.copy()
new_image = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Gray image', gray)  
cv2.waitKey(0) 
cv2.destroyAllWindows() 
 
# Convert the grayscale image to binary
ret, binary = cv2.threshold(gray, 100, 255,  cv2.THRESH_OTSU) 
cv2.imshow('Binary image', binary)
cv2.waitKey(0) 
cv2.destroyAllWindows() 
 
# To detect object contours, we want a black background and a white 
# foreground, so we invert the image (i.e. 255 - pixel value)
inverted_binary = ~binary
cv2.imshow('Inverted binary image', inverted_binary)
cv2.waitKey(0) 
cv2.destroyAllWindows() 
 
# Find the contours on the inverted binary image, and store them in a list
# Contours are drawn around white blobs.
# hierarchy variable contains info on the relationship between the contours
contours, hierarchy = cv2.findContours(inverted_binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
       
# Draw the contours (in red) on the original image and display the result
# Input color code is in BGR (blue, green, red) format
# -1 means to draw all contours
with_contours = cv2.drawContours(image, contours, -1,(255,0,255),3)
cv2.imshow('Detected contours', with_contours)
cv2.waitKey(0)
cv2.destroyAllWindows() 

#for r i.e red 
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower = np.array([0,50,50])
upper= np.array([30,255,255])
mask = cv2.inRange(hsv, lower, upper)
result = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('result', result)
cv2.waitKey(0) 

image = result.copy()
new_image = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Gray image', gray)  
cv2.waitKey(0) 
cv2.destroyAllWindows() 
 
# Convert the grayscale image to binary
ret, binary = cv2.threshold(gray, 100, 255,  cv2.THRESH_OTSU) 
cv2.imshow('Binary image', binary)
cv2.waitKey(0) 
cv2.destroyAllWindows() 
 
# To detect object contours, we want a black background and a white 
# foreground, so we invert the image (i.e. 255 - pixel value)
inverted_binary = ~binary
cv2.imshow('Inverted binary image', inverted_binary)
cv2.waitKey(0) 
cv2.destroyAllWindows() 
 
# Find the contours on the inverted binary image, and store them in a list
# Contours are drawn around white blobs.
# hierarchy variable contains info on the relationship between the contours
contours, hierarchy = cv2.findContours(inverted_binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
       
# Draw the contours (in red) on the original image and display the result
# Input color code is in BGR (blue, green, red) format
# -1 means to draw all contours
with_contours = cv2.drawContours(image, contours, -1,(255,0,255),3)
cv2.imshow('Detected contours', with_contours)
cv2.waitKey(0)
cv2.destroyAllWindows() 