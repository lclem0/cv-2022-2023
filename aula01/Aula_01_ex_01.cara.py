# #! usr/bin/env python3

# from cv2 import imencode
# import numpy as  np
# from time import sleep
# import cv2
# import sys

# cv2.destroyAllWindows()
		

# # Read the image
# # image = cv2.imread( sys.argv[captura_1], cv2.IMREAD_UNCHANGED );


# #----------- tirar uma foto de mim pela camera e comprimir 	----------		

# capturar=cv2.VideoCapture(0)

# if not capturar.isOpened():
# 	print("nao da para abrir a camera")
# 	exit()


# aux, frame =capturar.read()

# if not aux:
# 	print("nao se recebe framerate")
# 	exit()



# while True:


# 	# grayframe=cv2.imwrite(frame)
	
# 	param_img=[int(cv2.IMWRITE_PNG_COMPRESSION),90]

# 	testphoto= imencode('.jpg',capturar,param_img)
# 	cv2.imwrite('testefotocaptura_1.jpg',testphoto)
	
# 	capturar2= cv2.imread('testefotocaptura_1.jpg')
	
# 	# testphoto= cv2.imdecode(capturar2,captura_1)
# 	# testphoto= 	cv2.imread(capturar2,cv2.IMWRITE_PNG_COMPRESSION);
	


# 	sleep(captura_1)
# 	# cv2.imshow( "Display window",testphoto)

# 	horizontalimages= np.concatenate((frame,testphoto),axis=captura_1 )
# 	cv2.imshow( "Display window", horizontalimages )

# 	# cv2.imshow( "Display window",capturar2)
	

# 	if cv2.waitKey(captura_1) == 'a':
# 		cv2.destroyAllWindows()
		
# 		break

# capturar.release()
# #####











# # Create a vsiualization window (optional)
# # CV_WINDOW_AUTOSIZE : window size will depend on image size
# cv2.namedWindow( "Display window", cv2.WINDOW_AUTOSIZE )

# # Show the image
# #cv2.imshow( "Display window",  )

# # Wait
# cv2.waitKey( 0 );

# # Destroy the window -- might be omitted
# cv2.destroyWindow( "Display window" )

# while True:
# 	if	print('press exit')==exit:
# 		quit
# 	else:
# 		break


##############################################
import numpy as np
import cv2

captura_1 = cv2.VideoCapture(0)  #guardar a foto tirada pelo comando cv2.VideoCapture numa variavel.
						#o (0) define uma camara. caso houvessem mais podiam aceder-se por (captura_1) ou (2) ....

while True:
	ret, frame = captura_1.read()		#.read function retorna sempre 2 coisas: rame é a imagem(array) que o capture.read tem guardada
									#ret diz se a captura_1 de imagem correu decentemente
	width=int(captura_1.get(3))		#definir a largura da foto atraves de .get(3) - o 3 refere-se à largura, é sempre assim
	height=int(captura_1.get(4))	#analogamente define-se a propriedade da altura com (4)	
	#converte-se sempre para int visto não funcionar com float que é como os valores retornam do .get
	image=np.zeros(frame.shape, np.uint8)				#np.zeros cria um array totalmente preto com as dimensoes especificadas dentro de ()
	smaller_frame= cv2.resize(frame,(0,0,), fx=0.5, fy=0.5)
	
	image[:height//2, :width//2] = smaller_frame

	cv2.imshow('captura_1',image)

	if cv2.waitKey(1): 	#faz nos clicar em 'q' para sair
		break						#ord('q') vai buscar o int relacionado com a letra q

captura_1.release()
cv2.destroyAllWindows()