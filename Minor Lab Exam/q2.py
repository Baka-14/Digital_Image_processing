import cv2
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

img = cv2.imread('picture.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gaussian = cv2.GaussianBlur(gray,(3,3),0)

 
#canny
img_canny = cv2.Canny(img,100,200)


#robert 
  
roberts_cross_v = np.array( [[1, 0 ],
                             [0,-1 ]] )
  
roberts_cross_h = np.array( [[ 0, 1 ],
                             [ -1, 0 ]] )

img_r= cv2.imread("picture.png",0).astype('float64')
img_r/=255.0
vertical = ndimage.convolve( img_r, roberts_cross_v )
horizontal = ndimage.convolve( img_r, roberts_cross_h )
  
edged_img = np.sqrt( np.square(horizontal) + np.square(vertical))
edged_img*=255

cv2.imshow("Original Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Canny", img_canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("Robert",edged_img)
cv2.waitKey(0)
cv2.destroyAllWindows()  
plt.imshow(edged_img)
plt.title('Robert Edge')
plt.show()


