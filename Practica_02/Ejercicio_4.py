suma = 0
while True:
    print("Introduce un numero o fin para terminar")
    x = input()
    if x == "fin":
        break
    else :
        try:
            x = int(x)
            suma += x
        except ValueError:
            print("Debe ser un numero o fin")

print("La suma total es " + str(suma))