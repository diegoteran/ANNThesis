# la prealimentacion se reduce a multiplicacion de matrices
# por cada capa en la red neuronal para conseguir una salida
# por cada entrada
def prealimentacion(self, x):
	x = np.array([np.array(x)]).T

	# multiplica matrices, agrega parcialidades, aplica funcion de
	# activacion
	for b, w in zip(self.parcialidades, self.pesos):
		x = sigmoide(np.dot(w, x)+b)
	
	return x
