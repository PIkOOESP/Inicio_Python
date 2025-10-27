print("Introduce la temperatura")
temperatura = input()
while True :
    print("Introduce la conversion\n1.Celsius\n2.Fahrenheit")
    conversion = input()
    conversion = int(conversion)
    
    if conversion == 1 or conversion == 2 :
        break
    else :
        print("Debe seleccionar una de las opciones disponibles")

if conversion == 1 :
    print(str(temperatura) + "ºF = " + str((float(temperatura) - 32) * 5 / 9) + "ºC")
elif conversion == 2 :
    print(str(temperatura) + "ºC = " + str((float(temperatura) * 9 / 5) + 32) + "ºF")