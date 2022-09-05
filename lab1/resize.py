import cv2
import numpy as np

img=cv2.imread('wp3013104.jpeg')
h,w,c=img.shape
new_img=cv2.resize(img,(500,500))
cv2.imshow('image',new_img)

cv2.waitKey(0)

cv2.destroyAllWindows()
