# import
from pickletools import uint8
import sys
import numpy as np
import cv2


image = cv2.imread('art3.bmp', cv2.IMREAD_UNCHANGED )


#ret,image_neg = cv2.threshold(image,120,255,cv2.THRESH_BINARY_INV)
image_neg = cv2.bitwise_not(image)
#opening operation

kernel_circ = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11))    #kernel circular 11x11
image_open = cv2.morphologyEx(image_neg,cv2.MORPH_OPEN,kernel_circ)  #erosion image twice

cv2.imshow(" image",image)
cv2.imshow("circular kernel",image_open)


image2 = cv2.imread('art2.bmp', cv2.IMREAD_UNCHANGED )
image_neg2 = cv2.bitwise_not(image2)
kernel_rect =   cv2.getStructuringElement(cv2.MORPH_RECT,(3,9))  #kernel retangular 3x9
image_open2 = cv2.morphologyEx(image_neg2,cv2.MORPH_OPEN,kernel_rect)  

kernel_rect2 =  cv2.getStructuringElement(cv2.MORPH_RECT,(9,3))  #kernel retangular 9x3
image_open3 = cv2.morphologyEx(image_neg2,cv2.MORPH_OPEN,kernel_rect2)

cv2.imshow("rect 3x9",image_open2)
cv2.imshow("rect 9x3",image_open3)
cv2.waitKey(0)

