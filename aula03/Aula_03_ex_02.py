# Aula_03_ex_02.py
#
# Mean Filter - blur function
#
# Paulo Dias - 09/2021

#import
import sys
import numpy as np
import cv2

def printImageFeatures(image):
	# Image characteristics
	if len(image.shape) == 2:
		height, width = image.shape
		nchannels = 1
	else:
		height, width, nchannels = image.shape

	# print some features
	print("Image Height: %d" % height)
	print("Image Width: %d" % width)
	print("Image channels: %d" % nchannels)
	print("Number of elements : %d" % image.size)

# Read the image from argv
image = cv2.imread( sys.argv[1] , cv2.IMREAD_GRAYSCALE );
#image = cv2.imread( "./lena.jpg", cv2.IMREAD_GRAYSCALE );

if  np.shape(image) == ():
	# Failed Reading
	print("Image file could not be open!")
	exit(-1)

printImageFeatures(image)

cv2.imshow('Orginal', image)

# Average filter 3 x 3
image_Average_Filter3 = cv2.blur( image, (3, 3))
#Average filter 3 x 3
image_Average_Filter5 = cv2.blur( image, (5, 5))
image_Average_Filter7 = cv2.blur( image, (7,7))
horizontalimages= np.concatenate((image_Average_Filter3,image_Average_Filter5,image_Average_Filter7),axis=1 )
cv2.imshow( "Average Filter dif dimensions 1 iteration",horizontalimages )
cv2.waitKey(0)
image_iteration2 = cv2.blur( image_Average_Filter3, (3,3))
image_iteration3 = cv2.blur( image_iteration2, (3,3))
cv2.imshow( "Average Filter 3 iteration", image_iteration3)
cv2.waitKey(0)



