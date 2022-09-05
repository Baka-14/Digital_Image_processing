import cv2
img=cv2.imread('wp3013104.jpeg')
cv2.imshow('Original',img)
cv2.waitKey(0) 

red=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("changed",red)
cv2.waitKey(0)  

red=cv2.cvtColor(img,cv2.COLOR_BGR2LUV)
cv2.imshow("changed",red)
cv2.waitKey(0) 

red=cv2.cvtColor(img,cv2.COLOR_BGR2HLS)
cv2.imshow("changed",red)
cv2.waitKey(0) 

cv2.destroyAllWindows()