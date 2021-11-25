#2.read information of the image


import cv2
img = cv2.imread('123.jfif')
print(img.shape)
print("Height",int(img.shape[0]))# 0 is for height of image
print("Width",int(img.shape[1]))#1 is for width of image
