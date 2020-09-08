# Función que encripta el mensaje txt
def Encriptar(Texto, Niveles): 

	# Crea una matriz a partir de la palabra a cifrar y lo niveles de encriptación
	Matriz = [['\n' for i in range(len(Texto))] 
				for j in range(Niveles)] 
	
	# Se define un punto de inicio ligado a la matriz, en donde se empieza por el 0,0
	Bajar = False
	Fila = 0
	Columna = 0
	
	for i in range(len(Texto)): 
		
		# check the direction of flow 
		# reverse the direction if we've just 
		# filled the top or bottom Matriz 
		if (Fila == 0) or (Fila == Niveles - 1): 
			Bajar = not Bajar 
		
		# fill the corresponding alphabet 
		Matriz[Fila][Columna] = Texto[i] 
		Columna += 1
		
		# find the next Fila using 
		# direction flag 
		if Bajar: 
			Fila += 1
		else: 
			Fila -= 1
	# now we can construct the Texto_Cifrado 
	# using the Matriz matrix 
	Resultado = [] 
	for i in range(Niveles): 
		for j in range(len(Texto)): 
			if Matriz[i][j] != '\n': 
				Resultado.append(Matriz[i][j]) 
	return("" . join(Resultado)) 
	
# This function receives Texto_Cifrado-Texto 
# and Niveles and returns the original 
# Texto after decryption 
def Desencriptar(Texto_Cifrado, Niveles): 

	# create the matrix to Texto_Cifrado 
	# plain Texto Niveles = Filas , 
	# length(Texto) = Columnaumnas 
	# filling the Matriz matrix to 
	# distinguish filled spaces 
	# from blank ones 
	Matriz = [['\n' for i in range(len(Texto_Cifrado))] 
				for j in range(Niveles)] 
	
	# to find the direction 
	Bajar = None
	Fila, Columna = 0, 0
	
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
