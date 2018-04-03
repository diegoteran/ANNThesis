# Red Neuronal definida en una clase
class RedNeuronal(object):

    # Constructor de la red 
    def __init__(self, capas):
        """La lista ``capas`` contiene la cantidad de neuronas sigmoides
        que se utilizan en cada capa de la red.  Por ejemplo, si la lista
        es [4, 5, 2] entonces es una red con tres capas, la primer capa
        va a contener 4 neuronas, la segunda capa va a contener 5 neuronas,
        y la tercer capa 2 neuronas.  Las parcialidades y los pesos para la
        red neuronal se inician con numeros aleatorios, utilizando una distribucion
        normal con media 0, y varianza 1.  Notar que la primer capa se asume
        que es la capa de entrada y por covnencion no se le asignan parcialidades, 
        ya que las parcialidades solo se utilizan al computar las salidas de cada
        capa."""
        self.num_capas = len(capas)
        self.capas = capas
        self.parcialidades = [np.random.randn(y, 1) for y in capas[1:]]
        self.pesos = [np.random.randn(y, x)
                        for x, y in zip(capas[:-1], capas[1:])]
