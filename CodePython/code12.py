def evaluar(self, datos_prueba):
	"""Regresa el numero de entradas de prueba para los que la
	red neuronal tuvo la respuesta correcta. Notar que se asume
	que la respuesta es el valor mas alto en el vector de
	salida de la ultima capa."""
	resultados = [(self.prealimentacion(x), y)
					for (x, y) in datos_prueba]
	return sum(self.miComp(x, y) for (x, y) in resultados)
