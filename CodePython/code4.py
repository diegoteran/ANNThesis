palabras = []
clases = []
documentos = []
ignorar_palabras = ['?']

# iterar por cada pareja en los datos de entrenamiento
for pareja in datos_entrenamiento:
    if type(pareja['texto']) != str or type(pareja['clase']) != str:
        continue
        
    # separar el texto por palabras (tokenize)
    p = nltk.word_tokenize(pareja['texto'])
    
    # agregar la palabra a nuestra lista de palabras
    palabras.extend(p)
    
    # guardar lista de palabras con clase a documentos
    documentos.append((p, pareja['clase']))
    
    # guardar las diferentes clases en una lista de clases
    if pareja['clase'] not in clases:
        clases.append(pareja['clase'])

# hacer stemming, pasar a minusculas y eliminar duplicados
palabras = [stemmer.stem(p.lower()) for p in palabras if p not in ignorar_palabras]
palabras = list(set(palabras))

# quitar duplicados de clases
clases = list(set(clases))