import csv
import json

#Ejercicio 1

with open ("saludo.txt", "w") as fichero:
    fichero.write("Hola mundo")
    
    
with open ("saludo.txt", "r") as fichero:
    texto = fichero.read()

print(texto)


#Ejercicio 2

def registrar_evento(mensaje):
    with open ("log.txt", "a") as fichero:
        fichero.write(mensaje, "\n")
        
registrar_evento("Programa iniciado")
registrar_evento("Accion realizada")


#Ejercicio 3

def contar_lineas():
    with open("datos.txt", "r") as fichero:
        texto = fichero.readlines()
    print("Numero de lineas",len(texto))
    
contar_lineas()


#Ejercicio 4

numeros = [10,20,30]

with open("numeros.txt","w") as fichero:
    for n in numeros:
        fichero.write(str(n),"\n")

with open("numero.txt","r") as fichero:
    numero = fichero.readline()
    total = 0
    for r in numero:
        total += int(r.strip())
        
print("Suma total:", total)


#Ejercicio 5

with open("productos.csv","r") as fichero:
    productos = csv.reader(fichero)
    for p in productos:
        print("Producto: ", p[0],"- Precio: ", p[1])
        
#Ejercicio 6

usuarios =[
    {"nombre" : "Ana", "email" : "ana@test.com"},
    {"nombre" : "Luis" , "email" : "luis@test.com"}
]

with open("usuarios.csv", "w", newline="", encoding="UTF-8") as fichero:
    escritor = csv.writer(fichero)
    escritor.writerow("nombre", "email")
    escritor.writerows(usuarios)
    
    
#Ejercicio 7

with open("config.json","r") as fichero:
    f = json.load(fichero)
    
print("Modo actual:", f["modo"])


#Ejercicio 8

inventario = [
    {"nombre" : "Teclado", "precio" : 20.0, "stock" : 15},
    {"nombre" : "Raton", "precio" : 10.0, "stock" : 30}
]

with open("inventario.json", "w") as fichero:
    json.dump(inventario, fichero, indent = 4, ensure_ascii = False)