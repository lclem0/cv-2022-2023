# Aula_03_ex_03.py
#
# Mean Filter - medianblur
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


image_Average_Filter3 = cv2.medianBlur(image,5)

cv2.imshow('Median Blur', image_Average_Filter3)
cv2.waitKey(0)