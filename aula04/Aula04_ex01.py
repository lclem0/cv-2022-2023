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



kernel = np.ones((11,11),dtype="uint8")     #kernel 11x11
kernel_circ = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11)) #kernel circular 11x11
image_dil = cv2.dilate(image_neg,kernel_circ,iterations=2)  #dilating image twice
image_dil2 = cv2.dilate(image_dil,kernel,1)

cv2.imshow("image",image)
cv2.imshow("image_binary",image_binary)
cv2.imshow("image_neg",image_neg)
cv2.imshow("dilated image",image_dil)
cv2.imshow("dilated image2",image_dil2)
cv2.waitKey(0)
