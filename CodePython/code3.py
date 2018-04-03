# Se pasan los datos a formato para vectorizar
listaTexto = df["texto"].tolist()
listaClase = df["clase"].tolist()

datos_entrenamiento = []
for i in range(len(listaTexto)):
    datos_entrenamiento.append({"clase":listaClase[i], "texto":listaTexto[i]})
