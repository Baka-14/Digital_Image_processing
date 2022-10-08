import cv2
 
img = cv2.imread("wp3013104.jpeg")
img = cv2.resize(img, (680, 520),interpolation=cv2.INTER_CUBIC)
                 
hpf = img - cv2.GaussianBlur(img, (21, 21), 3)+127

cv2.imshow("Original", img) 
cv2.waitKey(0)
cv2.destroyAllWindows()  

cv2.imshow("High Passed Filter", hpf)
cv2.waitKey(0)
cv2.destroyAllWindows() 
