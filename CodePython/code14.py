#### Funciones logisticas para activacion de neuronas
def sigmoide(z):
    """La funcion sigmoide."""
    return 1.0/(1.0+np.exp(-z))

def sigmoide_derivada(z):
    """Derivada de la funcion sigmoide."""
    return sigmoide(z)*(1-sigmoide(z))