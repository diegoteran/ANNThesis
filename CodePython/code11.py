# Funcion para la comparacion contra salidas ideales binarias
def miComp(self, x, y):
	a = np.array(x).argmax()
	b = np.array(y).argmax()
	return int(np.array(x).argmax() == np.array(y).argmax())
