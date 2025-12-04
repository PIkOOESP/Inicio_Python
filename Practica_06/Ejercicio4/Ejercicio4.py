import json
import os

os.chdir(os.getcwd()+ "/Practica_06/Ejercicio4")

lista = []

if(os.path.exists("inventario.json")):
    with open ("inventario.json", "r", encoding="utf-8") as fichero:
        jotason = json.load(fichero)
        
lista.append(jotason)

# ---------- Funciones  ----------

def menu():
    print("===== INVENTARIO DE PRODUCTOS =====")
    print("1. Añadir nuevo producto")
    print("2. Buscar producto por nombre")
    print("3. Modificar precio o unidades")
    print("4. Mostrar informe")
    print("5. Guardar y salir")
    
def anadirProducto():
    nombre = input("Nombre: ").strip().lower()
    while True:
        try:
            precio = float(input("Precio: ").strip().lower())
            break
        except ValueError:
            print("Debe introducir un numero")

    while True:
        try:
            unidades = int(input("Unidades: ").strip().lower())
            break
        except:
            print("Debe introducirse un numero")
        
    categoria = input("Categoria: ").strip().lower()
    
    producto = {"nombre" : nombre, "precio" : precio, "unidades" : unidades, "categoria" : categoria}
    
    lista.append(producto)

def buscarNombre():
    if(lista is None):
        print("No hay datos que buscar")
        return
    
    nombre = input("Nombre: ").strip().lower()
    for l in lista:
        if nombre == l["nombre"]:
            print("Nombre: ",l["nombre"])
            print("Precio: ",l["precio"])
            print("Unidades: ",l["unidades"])
            print("Categoria: ",l["categoria"])

