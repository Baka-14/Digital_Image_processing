import cv2
import numpy as np

img1 = cv2.imread('wp3013104.jpeg') 
img2 = cv2.imread('butterfly.jpeg') 

N_img1=cv2.resize(img1,(500,500))
N_img2=cv2.resize(img2,(500,500))

cv2.imshow("Image-1",N_img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Image-2",N_img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

img_and=cv2.bitwise_and(N_img1,N_img2) 
cv2.imshow("Bitwise-AND",img_and)
cv2.waitKey(0)
cv2.destroyAllWindows()

img_or=cv2.bitwise_or(N_img1,N_img2)  
cv2.imshow("Bitwise OR",img_or)
cv2.waitKey(0)
cv2.destroyAllWindows()  


img_xor=cv2.bitwise_xor(N_img1,N_img2)  
cv2.imshow("Bitwise Ex-0R",img_xor)
cv2.waitKey(0)
cv2.destroyAllWindows()  

img_not=cv2.bitwise_not(N_img1,N_img2)
cv2.imshow("Bitwise Not",img_not)
cv2.waitKey(0)
cv2.destroyAllWindows()   

img_in1=cv2.imread('lab4/image1.png')
cv2.imshow("Image1",img_in1)
cv2.waitKey(0)
cv2.destroyAllWindows() 

img_in2=cv2.imread('lab4/iamge2.png')
cv2.imshow("Image2",img_in2)
cv2.waitKey(0)
cv2.destroyAllWindows()  

img_intersection=cv2.bitwise_and(img_in1,img_in2) 
cv2.imshow("Intersection of Two Images",img_intersection)
cv2.waitKey(0)
cv2.destroyAllWindows()   












