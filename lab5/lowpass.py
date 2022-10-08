import cv2
import numpy as np
from matplotlib import pyplot as plt 

img = cv2.imread('sunflower.jpeg')
blur = cv2.blur(img,(5,5)) 

mean_img=cv2.medianBlur(img,5) 
gauss_img=cv2.GaussianBlur(img,(5,5),0) 
median_img = cv2.medianBlur(img,5) 


cv2.imshow("Original image",img)
cv2.waitKey(0)
cv2.destroyAllWindows() 

cv2.imshow("Blurred image",blur)
cv2.waitKey(0)
cv2.destroyAllWindows()  


cv2.imshow("Mean low pass filter",mean_img)
cv2.waitKey(0)
cv2.destroyAllWindows() 

cv2.imshow("Gaussian low pass image",gauss_img)
cv2.waitKey(0)
cv2.destroyAllWindows()  

cv2.imshow("Median low pass image",median_img)
cv2.waitKey(0)
cv2.destroyAllWindows()   


 





