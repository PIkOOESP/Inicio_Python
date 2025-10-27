print("Introduce un nombre.")
nombre = input()

print("Introduce una edad.")
edad = input()

print("Introduce una ciudad.")
ciudad = input()

print("Introduce una profesion.")
profesion = input()

diccionario = {
    "nombre" : nombre,
    "ciudad" : ciudad,
    "edad" : edad, 
    "profesion" : profesion
}
print(diccionario)

print("Vuelve a introducir una ciudad.")
ciudad = input()

diccionario["ciudad"] = ciudad

print(diccionario)