import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt


###################
#Compute Histogram
####################
def compute_histogram(image,histSize, histRange):
	# Compute the histogram
	hist_item = cv2.calcHist([image], [0], None, [histSize], histRange)
	return hist_item

def compute_histogram2(image,histSize, histRange):
	# Compute the histogram
	hist_item = cv2.calcHist([image], [0], None, [histSize], histRange)
	return hist_item

##########################################
# Drawing with openCV
# Create an image to display the histogram
def histogram2image(hist_item, histSize, histImageWidth, histImageHeight, color):

	histImage = np.zeros((histImageWidth, histImageHeight, 1), np.uint8)

	# Width of each histogram bar
	binWidth = int(np.ceil(histImageWidth * 1.0 / histSize))

	# Normalize values to [0, histImageHeight]
	cv2.normalize(hist_item, hist_item, 0, histImageHeight, cv2.NORM_MINMAX)

	# Draw the bars of the nomrmalized histogram
	for i in range(histSize):
		cv2.rectangle(histImage, (i * binWidth, 0), ((i + 1) * binWidth, int(hist_item[i])), color, -1)

	# ATTENTION : Y coordinate upside down
	histImage = np.flipud(histImage)

	return histImage 




# Read the image from argv
image = cv2.imread( sys.argv[1] , cv2.IMREAD_UNCHANGED );
hist_eq = cv2.equalizeHist(image);

if  np.shape(image) == ():
	# Failed Reading
	print("Image file could not be open!")
	exit(-1)

# Image characteristics
if len (image.shape) > 2:
	print ("The loaded image is NOT a GRAY-LEVEL image !")
	exit(-1)

if  np.shape(hist_eq) == ():
	# Failed Reading
	print("Image file could not be open!")
	exit(-1)

# Image characteristics
if len (hist_eq.shape) > 2:
	print ("The loaded image is NOT a GRAY-LEVEL image !")
	exit(-1)

# Display the image
cv2.namedWindow("Original Image")
cv2.imshow("Original Image", image)
cv2.namedWindow("Equalized Image")
cv2.imshow("Equalized Image", hist_eq)



# cv2.imshow('smallest greatest',result)


# Size
histSize = 256	 # from 0 to 255
# Intensity Range
histRange = [0, 256]
histRange = [0, 256]
# Compute the histogram
hist_item = cv2.calcHist([image], [0], None, [histSize], histRange)
hist_item2 = cv2.calcHist([hist_eq], [0], None, [histSize], histRange)

##########################################
# Drawing with openCV
# Create an image to display the histogram
histImageWidth = 512
histImageHeight = 512
histImageWidth2 = 512
histImageHeight2 = 512
color = (125)
histImage = np.zeros((histImageWidth,histImageHeight,1), np.uint8)
histImage2 = np.zeros((histImageWidth2,histImageHeight2,1), np.uint8)


# Width of each histogram bar
binWidth = int (np.ceil(histImageWidth*1.0 / histSize))
binWidth2 = int (np.ceil(histImageWidth2*1.0 / histSize))


# Normalize values to [0, histImageHeight]
cv2.normalize(hist_item, hist_item, 0, histImageHeight, cv2.NORM_MINMAX)
cv2.normalize(hist_item2, hist_item2, 0, histImageHeight2, cv2.NORM_MINMAX)


# Draw the bars of the nomrmalized histogram
for i in range (histSize):
	cv2.rectangle(histImage,  ( i * binWidth, 0 ), ( ( i + 1 ) * binWidth, int(hist_item[i]) ), (125), -1)
for i in range(histSize):
    cv2.rectangle(histImage2,  ( i * binWidth2, 0 ), ( ( i + 1 ) * binWidth2, int(hist_item2[i]) ), (125), -1)


# ATTENTION : Y coordinate upside down
histImage = np.flipud(histImage)
histImage2 = np.flipud(histImage2)


cv2.imshow('colorhist_original', histImage)
cv2.imshow('colorhist equalized', histImage2)
cv2.waitKey(0)
