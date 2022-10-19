# Aula_03_ex_06.py
#
# Sobel Operator
#
# Paulo Dias - 09/2021

#import
import math
import sys
import numpy as np
import cv2

def printImageFeatures(image):
	# Image characteristics
	if len(image.shape) == 2:
		height, width = image.shape
		nchannels = 1;
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

grad_x = cv2.Sobel(image, cv2.CV_64F , 1, 0, ksize=3,  borderType=cv2.BORDER_DEFAULT) 
grad_y = cv2.Sobel(image, cv2.CV_64F , 0, 1, ksize=3,  borderType=cv2.BORDER_DEFAULT)
abs_grad_x = cv2.convertScaleAbs(grad_x)
abs_grad_y = cv2.convertScaleAbs(grad_y)
result = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

# Sobel Operatot 3 x 3
# imageSobel3x3_X = cv2.Sobel(image, cv2.CV_64F, 1, 0, 3)

#cv2.namedWindow( "Sobel 3 x 3 - X", cv2.WINDOW_AUTOSIZE )
# cv2.imshow( "Sobel 3 x 3 - X", imageSobel3x3_X )
# cv2.imshow( "8 bits - Sobel 3 x 3 - X", image8bits )
# image8bits = np.uint8( np.absolute(imageSobel3x3_X) )

#cv2.namedWindow( "64 bits", cv2.WINDOW_AUTOSIZE )
edges = cv2.Canny(image, 70,100)
image8bits = np.uint8( np.absolute(edges) )

#teste

cv2.imshow( "canny",edges )
#cv2.imshow( "canny-8bits",image8bits)
cv2.waitKey(0)
