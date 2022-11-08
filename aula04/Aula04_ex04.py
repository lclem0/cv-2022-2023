# import
from pickletools import uint8
import sys
import numpy as np
import cv2


image = cv2.imread('mon1.bmp', cv2.IMREAD_UNCHANGED )

#converter binario
ret,image_binary = cv2.threshold(image,120,255,cv2.THRESH_BINARY)

#converter negativo
#ret,image_neg = cv2.threshold(image,120,255,cv2.THRESH_BINARY_INV)
image_neg = cv2.bitwise_not(image_binary)


kernel_circ = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11))    #kernel circular 11x11
image_eroded = cv2.erode(image_neg,kernel_circ,iterations=2)  #erosion image twice
#quanto maior o numero de iterações, maior a diferença entre a imaem dilatada e a negativa
image_subs = cv2.subtract(image_neg,image_eroded)

kernel_rect = cv2.getStructuringElement(cv2.MORPH_RECT,(9,9))  #kernel retangular 9x9
image_eroded2 = cv2.erode(image_neg,kernel_rect,iterations=2)  
image_subs2 = cv2.subtract(image_neg,image_eroded2)

#cv2.imshow("image",image)
#cv2.imshow("image_binary",image_binary)
#cv2.imshow("image_neg",image_neg)
cv2.imshow("dilated image_circ",image_eroded)
cv2.imshow("dilated image_rect",image_eroded2)
cv2.imshow("subtraction image",image_subs)
cv2.imshow("subtraction image2",image_subs2)
cv2.waitKey(0)
