print("Introduce tu nombre")
nombre = input()
print ("Introduce tu edad")
edad = input()
edad = int(edad)
print ("Introduce tu altura(metros)")
altura = input()
altura = float(altura)
print("¿Estas trabajando?")
trabajo = input()

if trabajo.lower == "no" :
    trabajo = bool(False)
elif trabajo.lower == "si" :
    trabajo = bool(True)

print("El usuario " + nombre + " tiene " + str(edad) + " años, mide " + str(altura) + "m es", end=" ")

if edad < 18 :
    print ("menor de edad y" , end = " ")
else :
    print ("mayor de edad y" , end = " ")

if trabajo == True :
    print ("trabaja")
else : 
    print ("no trabaja")