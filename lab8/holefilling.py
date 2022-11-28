import cv2 
from PIL import Image
import numpy as np
from scipy import ndimage
from skimage.feature import peak_local_max
from skimage.segmentation import watershed

image = cv2.imread("picture.png")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
darker = cv2.equalizeHist(gray)
ret,thresh = cv2.threshold(darker,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
newimg = cv2.bitwise_not(thresh)

im2, contours, hierarchy = cv2.findContours(newimg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    cv2.drawContours(newimg,[cnt],0,255,-1) 

D = ndimage.distance_transform_edt(newimg)
localMax = peak_local_max(D, indices=False, min_distance=20, labels=thresh)
markers = ndimage.label(localMax, structure=np.ones((3, 3)))[0]
labels = watershed(-D, markers, mask=newimg)
print("[INFO] {} unique segments found".format(len(np.unique(labels)) - 1))