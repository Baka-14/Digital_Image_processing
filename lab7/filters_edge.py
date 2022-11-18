import cv2
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

img = cv2.imread('picture.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gaussian = cv2.GaussianBlur(gray,(3,3),0)

#laplacian Edge 
image = cv2.GaussianBlur(img, (3, 3), 0)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
lap = cv2.Laplacian(image_gray, cv2.CV_16S, ksize=3)
abs_lap = cv2.convertScaleAbs(lap) 

#canny
img_canny = cv2.Canny(img,100,200)

#sobel
img_sobelx = cv2.Sobel(img_gaussian,cv2.CV_8U,1,0,ksize=5)
img_sobely = cv2.Sobel(img_gaussian,cv2.CV_8U,0,1,ksize=5)
img_sobel = img_sobelx + img_sobely


#prewitt
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)

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
cv2.imshow("Laplacian", abs_lap)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("Canny", img_canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("Sobel X", img_sobelx)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("Sobel Y", img_sobely)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("Sobel", img_sobel)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("Prewitt X", img_prewittx)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("Prewitt Y", img_prewitty)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("Prewitt", img_prewittx + img_prewitty)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("Robert",edged_img)
cv2.waitKey(0)
cv2.destroyAllWindows()  
plt.imshow(edged_img)
plt.title('Robert Edge')
plt.show()


