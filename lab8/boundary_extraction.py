import cv2
 
image = cv2.imread("wp3013104.jpeg")
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
 