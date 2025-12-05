import json
import os

os.chdir(os.getcwd()+ "/Practica_06/Ejercicio4")

lista = []

if(os.path.exists("inventario.json")):
    with open ("inventario.json", "r", encoding="utf-8") as fichero:
        jotason = json.load(fichero)
        if(len(jotason)>1):
            lista = jotason
        else:
            lista.append(jotason)
    
print(lista)
# ---------- Funciones  ----------

def menu():
    print("===== INVENTARIO DE PRODUCTOS =====")
    print("1. Añadir nuevo producto")
    print("2. Buscar producto por nombre")
    print("3. Mostrar informe")
    print("4. Guardar y salir")
    
def anadirProducto(lista):
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

def buscarNombre(lista):
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

            while True:
                print("Quieres modificar el precio?")
                print("1.Si\n2.No")
                opcion1 = input("Opcion: ")

                if opcion1 == "1":
                    while True:
                        try:
                            precio = float(input("Precio: ").strip())
                            break
                        except ValueError:
                            print("Introduce un numero")

                if opcion1 == "2":
                    break

                else:
                    print("Debe introducir una opcion valida")
            
            while True:
                print("Quieres modificar las unidades?")
                print("1.Si\n2.No")
                opcion2 = input("Opcion: ")
                
                if opcion2 == "1":
                    while True:
                        try:
                            precio = int(input("Unidades: ").strip())
                            break
                        except ValueError:
                            print("Introduce un numero")
                if opcion1 == "2":
                    break

                else:
                    print("Debe introducir una opcion valida")
        

def informe(lista):
    n_productos = len(lista)

    precio_total = 0
    precio_alto = 0

    stock_menor = lista[0]["unidades"]
    producto_bajo = lista[0]["nombre"]

    for l in lista:
        precio_total += l["precio"]
        if precio_alto < l["precio"]:
            precio_alto = l["precio"]
            producto_alto = l["nombre"]

        if stock_menor > l["unidades"]:
            stock_menor = l["unidades"]
            producto_bajo = l["nombre"]

    print("Numero de productos: ", n_productos)
    print("Valor total del inventario: ", precio_total)
    print("Producto más caro: ", producto_alto, " ", precio_alto)
    print("Producto con menos stock: ", producto_bajo, " ", stock_menor)

def guardar(lista):
    with open("inventario.json", "w", encoding="utf-8") as fichero:
        json.dump(lista, fichero, indent=4, ensure_ascii=False)
        print("Guardado")


# --------- Main ---------

while True:
    menu()

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        anadirProducto(lista)
    elif opcion == "2":
        buscarNombre(lista)
    elif opcion == "3":
        informe(lista)
    elif opcion == "4":
        guardar(lista)
        print("Saliendo...")
        break     
    else: 
        print("Opcion no valida")
