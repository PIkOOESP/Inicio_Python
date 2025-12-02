import string
from collections import Counter
import os

# Esta direccion se debe cambiar si el programa no funciona
os.chdir(os.getcwd()+ "/Practica_06/Ejercicio2")

with open("laVeredaDeLaPuertaDeAtras.txt", 'r', encoding='utf-8') as fichero:
        texto = fichero.read()

# Numero de lineas
lineas = texto.splitlines()
n_lineas = len(lineas)

texto = texto.replace('\n', ' ').replace('\r', '').lower()
texto = texto.translate(str.maketrans('', '', string.punctuation))

# Numero de palabras
palabras = texto.split()
n_palabras = len(palabras)

# Top 5 palabras mas repetidas
contador_palabras = Counter(palabras)
top5 = contador_palabras.most_common(5)

# Numero de vocales, consonantes y longitud media de palabras
consonantes = "qwrtypsdfghjklñzxcvbnm"
vocales = "aeiou"
n_vocales = 0
n_consonantes = 0
longitud_total = 0

for i in range(len(palabras)):
        longitud_total += len(palabras[i])
        for a in range(len(palabras[i])):
                if(palabras[i][a] in vocales):
                        n_vocales += 1
                
                if(palabras[i][a] in consonantes):
                        n_consonantes += 1

longitud_media = longitud_total/n_palabras

# Palabra buscada por el usuario
buscar = input("Introduce la palabra que quieres buscar: ").strip().lower()
n_apariciones = palabras.count(buscar)

with open('estadisticas.txt', 'w', encoding='utf-8') as output_file:
        output_file.write("Número de palabras: "+ str(n_palabras) + "\n")
        output_file.write("Número de líneas: " + str(n_lineas) + "\n")
        output_file.write("Top 5 palabras más repetidas:\n")
        for palabra, cantidad in top5:
            output_file.write(palabra + ":" + str(cantidad)+"\n")
        output_file.write("Número de vocales: " + str(n_vocales) + "\n")
        output_file.write("Número de consonantes: " + str(n_consonantes) + "\n")
        output_file.write("Longitud media de las palabras: " + str(longitud_media) + "\n")
        output_file.write("El número de veces que aparece " + buscar + ": " + str(n_apariciones) + "\n")

print("Estadísticas generadas en 'estadisticas.txt'.")