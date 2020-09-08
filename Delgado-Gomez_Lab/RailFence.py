# Función que encripta el mensaje txt
def Encriptar(Texto, Niveles): 

	# Crea una matriz a partir de la palabra a cifrar y los niveles de encriptación
	Matriz = [['\n' for i in range(len(Texto))]  #Eje X
				for j in range(Niveles)]  #Eje Y
	
	# Se define un punto de inicio ligado a la matriz, en donde se empieza por el 0,0
	Bajar = False
	Fila = 0
	Columna = 0
	
	for i in range(len(Texto)): 
		
		#No baja la letra si es la primera
		if (Fila == 0) or (Fila == Niveles - 1): 
			Bajar = not Bajar 
		
		Matriz[Fila][Columna] = Texto[i] #Que escriba en la posición de la matriz la letra que se encuentra en ese instante
		Columna += 1
		
		#Al agregar una letra que aumente la posición de la fila
		if Bajar: 
			Fila += 1
		else: 
			Fila -= 1
	 
	Resultado = [] #Lista en donde se alojan las letras en el orden de encriptación según el nivel del rail fence 
	for i in range(Niveles): 
		for j in range(len(Texto)): 
			if Matriz[i][j] != '\n': 
				Resultado.append(Matriz[i][j]) 
	return("" . join(Resultado)) #Intersecta las letras correspondientes a la lista resultado
	
#Esta función se encarga de desencriptar el txt
def Desencriptar(Texto_Cifrado, Niveles): 

	# Crea una matriz a partir de la palabra a cifrar y los niveles de encriptación
	Matriz = [['\n' for i in range(len(Texto))]  #Eje X
				for j in range(Niveles)]  #Eje Y
	
	# Se define un punto de inicio ligado a la matriz, en donde se empieza por el 0,0
	Bajar = False
	Fila = 0
	Columna = 0
	
	# mark the places with '*' 
	for i in range(len(Texto_Cifrado)): 
		if Fila == 0: 
			Bajar = True
		if Fila == Niveles - 1: 
			Bajar = False
		
		# place the marker 
		Matriz[Fila][Columna] = '*'
		Columna += 1
		
		# find the next Fila 
		# using direction flag 
		if Bajar: 
			Fila += 1
		else: 
			Fila -= 1
			
	# now we can construct the 
	# fill the Matriz matrix 
	Indice = 0
	for i in range(Niveles): 
		for j in range(len(Texto_Cifrado)): 
			if ((Matriz[i][j] == '*') and
			(Indice < len(Texto_Cifrado))): 
				Matriz[i][j] = Texto_Cifrado[Indice] 
				Indice += 1
		
	# now read the matrix in 
	# zig-zag manner to construct 
	# the Resultadoant Texto 
	Resultado = [] 
	Fila, Columna = 0, 0
	for i in range(len(Texto_Cifrado)): 
		
		# check the direction of flow 
		if Fila == 0: 
			Bajar = True
		if Fila == Niveles-1: 
			Bajar = False
			
		# place the marker 
		if (Matriz[Fila][Columna] != '*'): 
			Resultado.append(Matriz[Fila][Columna]) 
			Columna += 1
			
		# find the next Fila using 
		# direction flag 
		if Bajar: 
			Fila += 1
		else: 
			Fila -= 1
	return("".join(Resultado)) 
