print ("Introduce un numero")
x = input()
x = int(x)
while True :
    print ("Introduce el segundo numero")
    y = input()
    y = int(y)
    
    if y != 0 :
        break
    else :
        print("El segundo numero debe ser distinto de 0")

print("Multiplicacion: " + str(x) + "*" + str(y) + " = " + str(x * y))
print("Suma: " + str(x) + "+" + str(y) + " = " + str(x + y))
print("Resta: " + str(x) + "-" + str(y) + " = " + str(x - y))
print("Division: " + str(x) + "/" + str(y) + " = " + str(x / y))