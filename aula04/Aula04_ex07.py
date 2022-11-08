# import
from pickletools import uint8
import sys
import numpy as np
import cv2


image = cv2.imread('lena.jpg', cv2.IMREAD_UNCHANGED )


ret,image_neg = cv2.threshold(image,120,255,cv2.THRESH_BINARY_INV)


height, width = image_neg.shape[:2]
image_pixel_val = image_neg[430,30]
# image_pixel_newval= image_pixel_val-5
image_floodfill = image_neg.copy()
mask = np.zeros((height+2, width+2), np.uint8)
cv2.floodFill(image_floodfill, mask, (430,30), int(image_pixel_val-5))
image_floodfill_neg = cv2.bitwise_not(image_floodfill)

cv2.imshow(" image",image)
cv2.imshow('image_neg',image_neg)
cv2.imshow('image_floodfill',image_floodfill)
#cv2.imshow('image_floodfill_neg', image_floodfill_neg)

cv2.waitKey(0)
