import cv2 
img=cv2.imread('wp3013104.jpeg')
cv2.imshow('Original',img)
cv2.waitKey(0)
new_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("changed",new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
