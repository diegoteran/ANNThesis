def propagacion(self, x, y):
	"""Regresa una tupla ``(grad_b, grad_w)`` que representa el
	gradiente para la funcion de costo C_x.  ``grad_b`` y
	``grad_w`` son listas capa-a-capa de arreglos numpy, similar
	a ``self.parcialidades`` y ``self.pesos``."""
	
	grad_b = [np.zeros(b.shape) for b in self.parcialidades]
	grad_w = [np.zeros(w.shape) for w in self.pesos]
	
	# simple prealimentacion
	activacion = np.array([np.array(x)]).T
	activaciones = [x] # lista para todas las activaciones (salidas de cada capa)
	zs = [] # lista para todas las salidas sin funcion de activacion
	for b, w in zip(self.parcialidades, self.pesos):
		z = np.dot(w, activacion)+b
		zs.append(z)
		activacion = sigmoide(z)
		activaciones.append(activacion)
		
	# pasar para atras
	delta = self.costo_derivada(activaciones[-1], y) * \
		sigmoide_derivada(zs[-1])
	grad_b[-1] = delta
	grad_w[-1] = np.dot(delta, activaciones[-2].transpose())
	
	# Notar que la variable L abajo se utiliza de forma distinta
	# a la tesis.  El orden esta invertido. De esta forma se aprovecha
	# que Python permite usar indices negativos.
	for l in range(2, self.num_capas):
		z = zs[-l]
		sp = sigmoide_derivada(z)
		delta = np.dot(self.pesos[-l+1].transpose(), delta) * sp
		grad_b[-l] = delta
		if len(np.array(activaciones[-l-1]).shape) < 2:
			grad_w[-l] = np.dot(delta, np.array([activaciones[-l-1]]))
		else:
			grad_w[-l] = np.dot(delta, np.array(activaciones[-l-1]).T)
			
	return (grad_b, grad_w)
