import cv2
num=int(input("please enter your number"))

img_0=cv2.imread("butterfly.jpeg")
img_1=cv2.imread("wp3013104.jpeg")

if num==0:
    cv2.imshow("IMAGE-0",img_0)
    cv2.waitKey(0)
else:
    cv2.imshow("IMAGE_1",img_1)
    cv2.waitKey(0)

cv2.destroyAllWindows()

for i in range(num):
    print("iam in loop and this is the ",i)
