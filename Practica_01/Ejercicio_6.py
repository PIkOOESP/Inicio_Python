contador, a, e, i, o, u = 0, 0, 0, 0, 0, 0

print("Introduce una frase")
frase = input()

while len(frase) > contador :
    conteo = frase[contador].lower()
    if conteo == "a" :
        a += 1
    elif conteo == "e" :
        e += 1
    elif conteo == "i" :
        i += 1
    elif conteo == "o" :
        o += 1 
    elif conteo == "u" :
        u += 1

    contador +=1
    
print("Numero de vocales:")
print("- A aparece " + str(a) + " veces")
print("- E aparece " + str(e) + " veces")
print("- I aparece " + str(i) + " veces")
print("- O aparece " + str(o) + " veces")
print("- U aparece " + str(u) + " veces")