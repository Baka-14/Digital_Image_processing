import cv2
import numpy as np 

img1=cv2.imread("lab3/banana.png")
img2=cv2.imread("lab3/apple.png") 

#can only add images of same size 
N_img1=cv2.resize(img1,(500,500))
N_img2=cv2.resize(img2,(500,500))
img_sum=cv2.add(N_img1,N_img2) 
img_subtract=cv2.subtract(N_img1,N_img2)
img_mul=cv2.multiply(N_img1,N_img2)
img_div=cv2.divide(N_img1,N_img2)

cv2.imshow('Addition',img_sum)
cv2.waitKey(0)
cv2.destroyAllWindows()  
cv2.imshow('Subtraction',img_subtract)
cv2.waitKey(0)
cv2.destroyAllWindows()  
cv2.imshow('Multiplication',img_mul)
cv2.waitKey(0)
cv2.destroyAllWindows() 
cv2.imshow('Divison',img_div)
cv2.waitKey(0)
cv2.destroyAllWindows() 

#numpy implementation
added_img=N_img1+N_img2 
sub_img=N_img1-N_img2
mul_img=N_img1*N_img2
div_img=N_img1/N_img2

cv2.imshow('Addition',added_img)
cv2.waitKey(0)
cv2.destroyAllWindows()  
cv2.imshow('Subtraction',sub_img)
cv2.waitKey(0)
cv2.destroyAllWindows() 
cv2.imshow('Multiplication',mul_img)
cv2.waitKey(0)
cv2.destroyAllWindows() 
cv2.imshow('Divison',div_img)
cv2.waitKey(0)
cv2.destroyAllWindows() 

