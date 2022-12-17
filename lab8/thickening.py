import cv2
import numpy as np                                                                                                                         
import matplotlib.pyplot as plt

mask = np.zeros((200,200,3), dtype=np.uint8)
cv2.line(mask, (50, 100), (150, 100), (255,255,255), 1)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
dilate = cv2.dilate(mask, kernel, iterations=5)
plt.imshow(mask)
plt.title('Original Line')
plt.show()
plt.imshow(dilate)
plt.title('Thickened Line')
plt.show()
