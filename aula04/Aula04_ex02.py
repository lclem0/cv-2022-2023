# import
from pickletools import uint8
import sys
import numpy as np
import cv2


image = cv2.imread(sys.argv[1], cv2.IMREAD_UNCHANGED )

#converter binario
ret,image_binary = cv2.threshold(image,120,255,cv2.THRESH_BINARY)

#converter negativo
#ret,image_neg = cv2.threshold(image,120,255,cv2.THRESH_BINARY_INV)
image_neg = cv2.bitwise_not(image_binary)


kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))    #kernel quadrado 3x3
image_dil = cv2.dilate(image_neg,kernel,iterations=1)  #dilating image once
image_subs = cv2.subtract(image_dil,image_neg)  #subtraction image

cv2.imshow("image",image)
cv2.imshow("image_binary",image_binary)
cv2.imshow("image_neg",image_neg)
cv2.imshow("dilated image",image_dil)
cv2.imshow("subtraction image",image_subs)
cv2.waitKey(0)
