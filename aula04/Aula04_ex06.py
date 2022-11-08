# import
from pickletools import uint8
import sys
import numpy as np
import cv2


image = cv2.imread('art4.bmp', cv2.IMREAD_UNCHANGED )


#ret,image_neg = cv2.threshold(image,120,255,cv2.THRESH_BINARY_INV)
image_neg = cv2.bitwise_not(image)
#opening operation

kernel_circ = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(22,22))    #kernel circular 22x22
kernel_circ2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,1))    #kernel circular 11x11
kernel_rect = cv2.getStructuringElement(cv2.MORPH_RECT,(9,9))  #kernel retangular 9x9

image_close = cv2.morphologyEx(image_neg,cv2.MORPH_CLOSE,kernel_circ)  #erosion image twice
image_close2 = cv2.morphologyEx(image_neg,cv2.MORPH_CLOSE,kernel_circ2)  #erosion image twice
image_close3 = cv2.morphologyEx(image_neg,cv2.MORPH_CLOSE,kernel_rect)  #erosion image twice

cv2.imshow(" image",image)
cv2.imshow("closed circular 22x22",image_close)
cv2.imshow('closed circular 11x11',image_close2)
cv2.imshow('closed rectangular 9x9',image_close3)


cv2.waitKey(0)
