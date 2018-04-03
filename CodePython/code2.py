# Para el manejo de bases de datos
import pandas as pd
dataframe = pd.read_csv("textosPruebas2.csv", error_bad_lines=False)

# Pasar datos al formato vector de parejas (texto, clase)
col1 = []
col2 = []

for i in range(len(dataframe)):
    texto1 = dataframe.iloc[i, 0]
    texto2 = dataframe.iloc[i, 1]
    clase = dataframe.iloc[i, 3]
    
    # Dos textos porque en esta base de datos se tienen
    # lugares vacios repartidos en dos columnas
    if (type(texto1) == float) and (math.isnan(texto1)):
            col1.append(texto2)
            col2.append(clase)
    else:
            col1.append(texto1)
            col2.append(clase)
            
columns = ['texto', 'clase']
index = range(len(col2))

# Se tiene el vector de parejas
df = pd.DataFrame(
    {
        'texto': col1,
        'clase': col2
    }, index = index, columns = columns
)