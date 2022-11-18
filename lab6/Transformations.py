import numpy as np
import cv2 as cv
img = cv.imread('galaxy.jpeg',0)
cv.imshow("Original",img) 
cv.waitKey(0) 
cv.destroyAllWindows() 

#Transalition
rows,cols = img.shape
M = np.float32([[1,0,100],[0,1,50]])
dst = cv.warpAffine(img,M,(cols,rows))
cv.imshow('Translation image',dst)
cv.waitKey(0)
cv.destroyAllWindows() 

#Scaledimage
res = cv.resize(img,None,fx=2.75, fy=2.5, interpolation = cv.INTER_CUBIC) 
cv.imshow("Scaled Image",res) 
cv.waitKey(0) 
cv.destroyAllWindows() 

#Rotation
dip= cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
rt= cv.warpAffine(img,dip,(cols,rows)) 
cv.imshow("Rotated Image",rt) 
cv.waitKey(0) 
cv.destroyAllWindows() 

#shrinking and zooming 
shrink = cv.resize(img,None,fx=0.25, fy=0.25, interpolation = cv.INTER_AREA) 
cv.imshow("Shrinking",shrink) 
cv.waitKey(0) 
cv.destroyAllWindows()  

zoom= cv.resize(img,None,fx=2, fy=2, interpolation = cv.INTER_LINEAR) 
cv.imshow("Zooming",zoom) 
cv.waitKey(0) 
cv.destroyAllWindows()  
