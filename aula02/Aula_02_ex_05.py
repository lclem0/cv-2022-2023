import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt




# Read the image from argv
image = cv2.imread( sys.argv[1] , cv2.IMREAD_UNCHANGED );
contrast_image = image.copy()


height , width = contrast_image.shape
# min = print(image.min())
# max = print(image.max())
min_max = cv2.minMaxLoc(contrast_image)




# cv2.imshow('smallest greatest',result)
 
if  np.shape(image) == ():
	# Failed Reading
	print("Image file could not be open!")
	exit(-1)

# Image characteristics
if len (image.shape) > 2:
	print ("The loaded image is NOT a GRAY-LEVEL image !")
	exit(-1)


# cv2.imshow('smallest greatest',result)


# Size
histSize = 256	 # from 0 to 255
# Intensity Range
histRange = [0, 256]
hist_Range_eq = [min_max,min_max]
# Compute the histogram
hist_item = cv2.calcHist([image], [0], None, [histSize], histRange)

##########################################
# Drawing with openCV
# Create an image to display the histogram
histImageWidth = 512
histImageHeight = 512
color = (125)
histImage = np.zeros((histImageWidth,histImageHeight,1), np.uint8)

# Width of each histogram bar
binWidth = int (np.ceil(histImageWidth*1.0 / histSize))

# Normalize values to [0, histImageHeight]
cv2.normalize(hist_item, hist_item, 0, histImageHeight, cv2.NORM_MINMAX)

# Draw the bars of the nomrmalized histogram
for i in range (histSize):
	cv2.rectangle(histImage,  ( i * binWidth, 0 ), ( ( i + 1 ) * binWidth, int(hist_item[i]) ), (125), -1)

# ATTENTION : Y coordinate upside down
histImage = np.flipud(histImage)


# Show the image
horizontalimages= np.concatenate((image,contrast_image),axis=1 )
cv2.imshow( "Images", horizontalimages)
cv2.waitKey(0)

