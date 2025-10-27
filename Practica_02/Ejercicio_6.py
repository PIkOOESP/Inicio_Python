contador = 0
consonante = 0
vocal = 0
numero = 0
vocales = "aaeiouáéíóúü"

print("Introduce una frase")
frase = input()

while contador < len(frase):
    if frase[contador].isalpha():
        if frase[contador] in vocales:
            vocal += 1
        else :
            consonante += 1
    elif frase[contador].isdigit() :
        numero += 1
    
    contador += 1

print("Hay " + str(consonante) + " consonantes, " + str(vocal) + " vocales y " + str(numero) + " numeros") 