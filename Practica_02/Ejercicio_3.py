pares = 0
impares = 0
for i in range(10):
    print("Introduce un numero")
    x = input()
    x = int(x)
    if(x % 2 == 0):
        pares += 1 
    else :
        impares += 1
    
print("Hay " + str(pares) + " numeros pares y " + str(impares) + " numeros impares")