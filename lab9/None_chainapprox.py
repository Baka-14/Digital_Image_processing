import cv2
import matplotlib.pyplot as plt

image = cv2.imread('sunflower.jpeg')
cv2.imshow("Original Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#padding since the t-shirt is touching the border, without this we cant get a continious contour around it.
image = cv2.copyMakeBorder(image, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=[255, 255, 255])
imgray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
imgray = cv2.GaussianBlur(imgray, (9, 9), 0)
ret, thresh = cv2.threshold(imgray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
img2=cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
cv2.imshow("Chain Aprrox NONE",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
