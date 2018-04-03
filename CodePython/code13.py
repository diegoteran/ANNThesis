def costo_derivada(self, activaciones_salida, y):
	y = np.array([np.array(y)]).T
	"""Regresa el vector de derivadas parciales de C_x
	para la salida de la red neuronal."""
	return (activaciones_salida-y)
