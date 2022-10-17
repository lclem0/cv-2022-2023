
#import


import numpy as np
import cv2
import sys


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




# Read the image
image_rgb = cv2.imread( sys.argv[1], cv2.IMREAD_UNCHANGED )
image_b,image_g,image_r = cv2.split(image_rgb)
image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY)



if  np.shape(image_rgb) == ():

	# Failed Reading
	print("Image file could not be open")
	exit(-1)

images = [image_rgb,image_gray,image_b,image_g,image_r]
hist_items =[]
histImageWidth = 512
histImageHeight = 512
color = (125)
histSize = 256	 
histRange = [0, 256]
histImages = []

for i in range(len(images)):
	hist_item = compute_histogram(images[i],histSize,histRange)
	hist_items.append(hist_item)

for i in range(len(hist_items)):
	histImage = histogram2image(hist_items[i],histSize, histImageWidth, histImageHeight, (125)) 
	histImages.append(histImage)


for i in range(len(images)):
	for i in range(len(histImages)):
		cv2.imshow('images', images[i])
		cv2.imshow('hist_[i]',histImages[i])
		cv2.waitKey(0)	
	

