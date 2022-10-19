
#import
import numpy as np
import cv2
import sys

# Read the image
image = cv2.imread( sys.argv[1], cv2.IMREAD_UNCHANGED )

if  np.shape(image) == ():
	# Failed Reading
	print("Image file could not be open")
	exit(-1)


ret,thresh1 = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(image,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV)


images = [thresh1,thresh2,thresh3,thresh4,thresh5]

for i in range(len(images)):
    cv2.imshow('images', images[i])
    cv2.waitKey(0)	
	

