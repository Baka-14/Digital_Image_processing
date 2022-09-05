import cv2
img=cv2.imread('butterfly.jpeg')
cv2.imshow("original",img)
cv2.waitKey(0)
img_neg=225-img
cv2.imshow("negative",img_neg)
cv2.waitKey(0)
cv2.destroyAllWindows() 
#convert to black and white 
