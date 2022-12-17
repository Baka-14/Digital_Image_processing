import cv2
import numpy as np                                                                                                                                                                             
import matplotlib.pyplot as plt 
                                                                                                        
img = cv2.imread("sunflower.jpeg",0)  
cv2.imshow("Original Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

ret,img = cv2.threshold(img, 127, 255, 0)   

size = np.size(img)
skel = np.zeros(img.shape, np.uint8)
element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
while True:
    open = cv2.morphologyEx(img, cv2.MORPH_OPEN, element)
    temp = cv2.subtract(img, open)
    eroded = cv2.erode(img, element)
    skel = cv2.bitwise_or(skel,temp)
    img = eroded.copy()
    if cv2.countNonZero(img)==0:
        break

plt.imshow(skel)
plt.title('Skeleton of Image')
plt.show()
