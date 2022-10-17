import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt


def compute_histogram(image,histSize, histRange):
	# Compute the histogram
	hist_item = cv2.calcHist([image], [0], None, [histSize], histRange)
	return hist_item

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

def contrast_stretch(image,x,y):
	value = cv2.minMaxLoc(image)
	newimage = image.copy()

	for i in range(x):
		for j in range(y):
			newimage[i,j]=newimage[i,j]-value[0]/(value[1]-value[0])*255
	return 	newimage


# Read the image from argv
image = cv2.imread( sys.argv[1] , cv2.IMREAD_UNCHANGED )

height, width = image.shape
nchannels = 1
print("Image Size: (%d,%d)" % (height, width))
print("Image Type: %d" % nchannels)
print("Number of elements : %d" % image.size) 

if  np.shape(image) == ():
	# Failed Reading
	print("Image file could not be open!")
	exit(-1)

# Image characteristics
if len (image.shape) > 2:
	print ("The loaded image is NOT a GRAY-LEVEL image !")
	exit(-1)

# Size
histSize = 256	 # from 0 to 255
# Intensity Range
histRange = [0, 256]


# Compute the histogram
hist_item = compute_histogram(image,histSize, histRange)
newimage = contrast_stretch(image,height,width)
height2, width2 = newimage.shape
hist_item_2 = compute_histogram(newimage,histSize, histRange)
##########################################
# Drawing with openCV
# Create an image to display the histogram
histImageWidth = 512
histImageHeight = 512
color = (125)
histImage =  histogram2image(hist_item, histSize, histImageWidth, histImageHeight, color)
histImage2 =  histogram2image(hist_item_2, histSize, histImageWidth, histImageHeight, color)

# Show the image
horizontalimages= np.concatenate((image,newimage),axis=1 )
horizontal_histograms = np.concatenate((histImage,histImage2),axis=1 ) 
cv2.imshow( "Images", horizontalimages)
cv2.imshow( "Histograms", horizontal_histograms)
cv2.waitKey(0)

