# crear los datos de entrenamiento vectorizados
entrenamiento = []
salidas = []
# crear un arreglo vacio para cada salida
salida_vacia = [0] * len(clases)

# los datos de entrenamiento utilizan el conjunto de
# palabras para crear cada vector binario
for doc in documentos:
    
    # inicializar la bolsa de palabras
    bolsa = []
    
    # lista de palabras para cada pareja en documentos
    pareja_palabras = doc[0]
    
    # stemmizar cada palabra
    pareja_palabras = [stemmer.stem(palabra.lower()) for palabra in pareja_palabras]
    
    # en nuestra bolsa se vectoriza con 1s o 0s dependiendo de 
    # si la palabra stemmizada se encuentra en nuestro conjunto
    for p in palabras:
        bolsa.append(1) if p in pareja_palabras else bolsa.append(0)

    # cada bolsa es una entrada para la red neuronal
    entrenamiento.append(bolsa)
    
    # se llena con 1 la posicion de la clase
    # todo lo que queda son 0s
    salida = list(salida_vacia)
    salida[clases.index(doc[1])] = 1
    salidas.append(salida)