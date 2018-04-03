def actualizar_mini_batch(self, mini_batch, eta):
	"""Actualiza los pesos y parcialidades de la red al utilizar
	descenso de gradiente con propagacion hacia atras a un solo
	mini batch. ``mini_batch`` es una lista de tuplas ``(x, y)``
	y ``eta`` es el learning rate."""
	
	grad_b = [np.zeros(b.shape) for b in self.parcialidades]
	grad_w = [np.zeros(w.shape) for w in self.pesos]
	for x, y in mini_batch:
		delta_nabla_b, delta_nabla_w = self.propagacion(x, y)
		grad_b = [nb+dnb for nb, dnb in zip(grad_b, delta_nabla_b)]
		grad_w = [nw+dnw for nw, dnw in zip(grad_w, delta_nabla_w)]
		
	self.pesos = [w-(eta/len(mini_batch))*nw
					for w, nw in zip(self.pesos, grad_w)]
					
	self.parcialidades = [b-(eta/len(mini_batch))*nb
				   for b, nb in zip(self.parcialidades, grad_b)]
