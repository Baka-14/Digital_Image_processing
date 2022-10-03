from skimage import io
from skimage import color
import numpy as np
from numpy.fft import fft, fftfreq, ifft
from scipy import ndimage as nd
from scipy.fft import fft, ifft
from scipy import fftpack
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import cv2


img = io.imread("butterfly.jpeg")
plt.imshow(img)
plt.show() 

# fft
img_fft =  fftpack.fft2(img)

# inverse of signal
img_ifft = fftpack.ifft2(img_fft).real

plt.figure(figsize=(10,10))

plt.subplot(131)
plt.imshow(img)
plt.title("Original")

plt.subplot(132)
plt.title("Spectrum")
plt.imshow(img_fft.astype(np.uint8))
plt.subplot(133)

plt.title("Reconstructed")
plt.imshow(img_ifft.astype(np.uint8))
plt.show()
 

plt.figure(figsize=(8, 6), constrained_layout=False)


img_fft = np.fft.fft2(img)
img_fftshift = np.fft.fftshift(img_fft)
img_ifftshit = np.fft.ifftshift(img_fftshift)
img_ifft = np.fft.ifft2(img_ifftshit)

plt.subplot(231), plt.imshow(img, "bone"), plt.title("Original Image")
plt.subplot(232), plt.imshow(np.abs(img_ifft), "bone"), plt.title("Reversed Image")
plt.show()