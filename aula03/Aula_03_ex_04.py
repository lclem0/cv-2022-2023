# Aula_03_ex_04.py
#
# Mean Filter - Gaussian blur
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
#image = cv2.imread( sys.argv[1] , cv2.IMREAD_GRAYSCALE );
image = cv2.imread( "./DETI_Ruido.png" , cv2.IMREAD_GRAYSCALE )

if  np.shape(image) == ():
	# Failed Reading
	print("Image file could not be open!")
	exit(-1)
    
printImageFeatures(image)

cv2.imshow('Orginal', image)


image_Average_Filter3 = cv2.GaussianBlur(image,(7,7),2,2,cv2.BORDER_DEFAULT)

cv2.imshow('Gaussian Blur', image_Average_Filter3)
cv2.waitKey(0)