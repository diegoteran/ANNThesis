# Para operaciones matematicas y otras aplicaciones
import math
import numpy as np

# uso de herramientas para procesamiento de lenguaje natural
import nltk

# Stemmer para lenguaje Ingles
# from nltk.stem.Lancaster import LancasterStemmer
# stemmer = LancasterStemmer()

# Stemmer para lenguaje Espanol
from nltk.stem.snowball import SpanishStemmer
stemmer = SpanishStemmer()

# Ejemplo de uso del stemmer, ambas respuestas son "visit"
# print(stemmer.stem("visitar"))
# print(stemmer.stem("visitantes"))