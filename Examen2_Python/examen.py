"""
Es un programa de gestion de libros en base a un archivo csv y json
"""
import csv
import json
import os
import datetime

# --------- Validacion de archivos ---------

CAMPOS=["id","titulo","autor","anio","estado"]
biblioteca = []
ultimoid = 0


if os.path.exists("libros.csv"):
    with open("libros.csv","r", encoding="utf-8") as fichero:
        reader = csv.DictReader(fichero)
        for r in reader:
            biblioteca.append(r)
            ultimoid = r["id"]

if os.path.exists("config.json"):
    with open("config.json", "r", encoding="utf-8") as fichero:
        config = json.load(fichero)

# --------- Funciones principales ---------

def menu():
    """ Es el menu principal del prgrama """
    print("==== Biblioteca ====")
    print("1. Añadir libro")
    print("2. Listar libros")
    print("3. Buscar libro por titulo")
    print("4. Eliminar libro")
    print("5. Guardar y salir")
    
def log(accion):
    """ Crea un mensaje en el log.txt con la accion, el dia de la fecha y la hora, tambien muestra un mensaje si el config.json lo dicta """
    mensaje = accion + ", " + str(datetime.datetime.now()) + "\n"
    with open("log.txt","a",encoding="utf-8") as fichero:
        fichero.write(mensaje)
    if(config["mostrar_logs"]):
        print("Log: ",mensaje)
    
def anadirLibro(lista, ultimoid):
    """ Añade un libro al csv de libros, teniendo en cuenta las validaciones que hay que hacer si esta el modo estricto activado """
    log("Añadir libro")
    ultimoid += 1
    id = ultimoid
    while True:
        titulo = input("Titulo: ").strip()
        
        if config["modo_estricto"]:
            if not titulo:
                print("El libro debe tener un titulo")
            else:
                break
        else:
            break
    
    while True:
        autor = input("Autor: ").strip()
        
        if config["modo_estricto"]:
            if not autor:
                print("El libro debe tener un autor")
            else:
                break
        else:
            break
        
    while True:
        try:
            anio = int(input("Año: "))
            if config["modo_estricto"]:
                if anio < 1500 or anio > int(datetime.datetime.now().strftime("%Y")):
                    print("El año debe estar entre 1500 y este año")
                else:
                    break
            else:
                break
        except ValueError:
            print("Debe introducirse un numero")
        
    estado = "Disponible"
    
    libro = {"id":id, "titulo":titulo, "autor":autor, "anio": anio, "estado":estado}
    
    lista.append(libro)
    
    guardarLibro(lista)
    
def guardarLibro(lista):
    """ Actualiza el csv cada vez que se hace un cambio en la lista de libros """
    log("Guardar libro")
    with open("libros.csv", "w", encoding="utf-8") as fichero:
        f = csv.DictWriter(fichero, fieldnames=CAMPOS)
        f.writeheader()
        f.writerows(lista)
        
def listaLibros(lista):
    """ Muesta la lista de todos los libros """
    log("Lista de libros")
    if not lista:
        print("No hay libros")
        return

    for l in lista:
        print(l["id"], "|", l["titulo"], "|", l["autor"], "|", l["anio"], "|", l["estado"])
        
def buscarLibro(lista):
    """ Busca un libro concreto y lo muestra, si no lo encuetra, muestra un mensaje de error """
    log("Buscar libro")
    if not lista:
        print("No hay libros")
        return
    
    titulo = input("Titulo: ").strip().lower()
    
    for l in lista:
        if l["titulo"].lower() == titulo:
            print(l["id"], "|", l["titulo"], "|", l["autor"], "|", l["anio"], "|", l["estado"])
            return
    
    print("Libro no encontrado")
    
    
def eliminarLibro(lista):
    """ Elimina un libro de la lista y actualiza el csv """
    log("Eliminar libro")
    
    if not lista:
        print("No hay lista")
        return
    
    titulo = input("Titulo: ").strip().lower()
    
    for i in range(len(lista)):
        if lista[i]["titulo"].lower() == titulo:
            lista.pop(i)
            guardarLibro(lista)
            return
        
    print("Libro no encontrado")
    
# -------- Programa principal ----------

while True:
    menu()
    
    opcion = input("Opcion: ").strip()
    
    if opcion == "1":
        anadirLibro(biblioteca,ultimoid)
    elif opcion == "2":
        listaLibros(biblioteca)
    elif opcion == "3":
        buscarLibro(biblioteca)
    elif opcion == "4":
        eliminarLibro(biblioteca)
    elif opcion == "5":
        guardarLibro(biblioteca)
        log("Saliendo del programa")
        print("Guardando todo y saliendo...")
        break
    else:
        print("Opcion no valida")