import cv2 
import numpy as np 

arr = np.random.randint(0, 256, (400,400), dtype=np.uint8)
_,bw_image = cv2.threshold(arr, 128,255,cv2.THRESH_BINARY)

cv2.imshow("2D array image",bw_image)
cv2.waitKey(0)
cv2.destroyAllWindows()