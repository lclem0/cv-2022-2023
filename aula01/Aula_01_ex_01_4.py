     # Aula_01_ex_01_4py
 #
 # Example of visualization of an image with openCV
 #
 # Paulo Dias - 09/2021



#import
import numpy as np
import cv2
import sys

# Read the image
#  -1, cv2.IMREAD_COLOR: carrega a imagem a cor. qualquer transparencia de imagem
#   0, cv2.IMREAD_GRAYSCALE: carrega a imagem a cinzento
#   1, cv2.IMREAD_UNCHANGED: carrega a imagem sem a modificar. se tiver transparencia vai continuar
 
image1 = cv2.imread(sys.argv[1], cv2.IMREAD_UNCHANGED )   #dá load numa imagem
image2 = cv2.imread(sys.argv[2], cv2.IMREAD_UNCHANGED )
image3 = image1.copy(cv2.IMREAD_GRAYSCALE)

if  np.shape(image1) == ():
	# Failed Reading
	print("Image file could not be open")
	exit(-1)

if  np.shape(image2) == ():
	# Failed Reading
	print("Image file could not be open")
	exit(-1)

#image3= cv2.subtract(image2,image1)

# Create a vsiualization window (optional)
# CV_WINDOW_AUTOSIZE : window size will depend on image size
cv2.namedWindow( "Display window", cv2.WINDOW_AUTOSIZE )


# Show the image
#cv2.imshow( "Display window", image)
horizontal_concat = np.concatenate((image1, image2, image3), axis=1)
cv2.imshow("Horizontal plot", horizontal_concat)  # cv2.imshow('Label_window', nome_variavel_imagem)


cv2.waitKey(0) 		# cv2.waitKey(0) 	espera infinitamente ate que seja fechad0 por ter o 0, se fosse 5 esperava 5 segundos
# Destroy the window -- might be omitted
cv2.destroyWindow("Display window")
print(image1.shape,image2.shape,image3.shape) #retorna o tamanho da imagem escolhida
# 336 linhas por 448 colunas por 3 layers (RGB)
#no opencv em vez de RED-GREEN-BLUE é usado BLUE-GREEN-RED (ordem alfabetica)

#Resize the image
#
# img = cv2.resize(img,(400,400))
# img = cv2.resize(img,(0,0), fx=0.5,fy=0.5)	da resize em que fx e fy sao a escala em função do tamanho original
#  neste caso necessita que (0,0) para se puder usar o fx e o fy
# 
# Rotate the image
# 
# img = cv2.rotate(img, cv2.cv2.ROTATE_180)		usa-se cv2.cv2.ROTATE e depois escolhe-se a opcao que se quer   

# Save the image
# cv2.imwrite('new_img.jpg', img)	guarda a img no novo ficheiro 'new_img.jpg'

###############Acessing pixel values

# print(img[257][400])	acede a linha 257 ao pixel 400 para ver as cores associadas a esse pixel

# for i in range(100):		#dar loop nas primeiras 100 linhas da imagem
#	for j in range(img.shape[1]):		#como .shape da toda a forma: [1] vai dar loop em todas as colunas das 100 linhas
#		img[i][j]=[0,0,0]

#copying parts of image:
# 	img = cv2.imread('image' , -1)
#	tag = img[100:500,200:350]      #atribuir uma variavel aos valores que queremos copiar
#		img[300:700,400:550] = tag 	#igualar os valores copiados antes aos pixeis que queremos da imagem inicial (tem que ter o mesmo tamanho)
#	cv2.imshow('Image', img)
#	cv2.waitKey(0)
#	cv2.destroyAllWindows()

