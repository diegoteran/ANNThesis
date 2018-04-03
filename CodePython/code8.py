# Algoritmo de Descenso de Gradiente Estocastico
def DGE(self, datos_entrenamiento, epocas, mini_batch_size, eta,
		datos_prueba=None):
	"""Entrena la red neuronal utilizando descenso de gradiente
	estocastico en mini-batchs.  Los ``datos_entrenamiento`` es una
	lista de tuplas ``(x, y)`` que representan las entradas y las
	salidas deseadas.  (eta es el learning rate.)  
	Si ``datos_prueba`` existe como parametro, se utiliza para que
	la red haga pruebas con los datos despues de cada epoca, 
	y se imprime el progreso en cada una.  Esto sirve para ver la
	red en funcionamiento, pero se vuelve mas lento el entrenamiento."""

	datos_entrenamiento = list(datos_entrenamiento)
	n = len(datos_entrenamiento)

	if datos_prueba:
		datos_prueba = list(datos_prueba)
		n_prueba = len(datos_prueba)

	for j in range(epocas):
		random.shuffle(datos_entrenamiento)
		mini_batches = [
			datos_entrenamiento[k:k+mini_batch_size]
			for k in range(0, n, mini_batch_size)]
		for mini_batch in mini_batches:
			self.actualizar_mini_batch(mini_batch, eta)
		if datos_prueba:
			print("Epoca {} : {} / {}".format(j,self.evaluar(datos_prueba),n_prueba));
		else:
			print("Epoca {} terminada".format(j))
