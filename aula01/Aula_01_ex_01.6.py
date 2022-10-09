 # Aula_01_ex_01.py
 #
 # Example of visualization of an image with openCV
 #
 # Paulo Dias - 09/2021



#import

import numpy as np
import cv2
import sys


# Read the image
image = cv2.imread( sys.argv[1], cv2.IMREAD_UNCHANGED );


if  np.shape(image) == ():
	# Failed Reading
	print("Image file could not be open")
	exit(-1)




foto2= cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)





# Create a vsiualization window (optional)
# CV_WINDOW_AUTOSIZE : window size will depend on image size
cv2.namedWindow( "Display window", cv2.WINDOW_AUTOSIZE )

# Show the image
# horizontalimages= np.concatenate((newimage,image,imagebmp),axis=1 )
cv2.imshow( "Display window", foto2)

# Wait
cv2.waitKey( 0 );

# Destroy the window -- might be omitted
cv2.destroyWindow( "Display window" )
