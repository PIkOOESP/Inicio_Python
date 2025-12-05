import re
import os
import csv
import json
import datetime

os.chdir(os.getcwd()+ "/Practica_06/Ejercicio5")

CAMPOS = ["id","nombre","email","edad","rol"]
lista = []

if os.path.exists("usuarios.csv"):
    with open("usuarios.csv","r", encoding="utf-8") as fichero:
        dicc = csv.DictReader(fichero)
        for d in dicc:
            lista.append(d)

if os.path.exists("config.json"):
    with open("config.json", "r", encoding="utf-8") as fichero:
        config = json.load(fichero)


# ---------- Funciones ----------

def menu():
    print("==== Mini-Base de Datos de Usuarios ====")
    print("1. Añadir usuario nuevo")
    print("2. Listar usuarios")
    print("3. Buscar usuario por email")
    print("4. Eliminar usuario")
    print("5. Modificar rol de usuario")
    print("6. Salir")

def anadirUsuario(lista):
    log("Añadir usuario")
    id = len(lista)
    nombre = input("Nombre: ").strip()
    
    while True:
        email = input("Email: ").strip()
        if(config["modo_estricto"]):
            if re.match(r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$', email):
                break
            else:
                print("El email no es válido")
        else:
            break
    
    while True:
        try:
            edad = int(input("Edad: ").strip())
            if(config["modo_estricto"]):
                if(edad > 16):
                    break
                else:
                    print("El usuario debe ser mayor de 16 años")
            else:
                break
        except ValueError:
            print("Se debe introducir un número")
    
    rol = input("Rol: ").strip()

    usuario = {"id":id,"nombre":nombre,"email":email,"edad":edad,"rol":rol}

    lista.append(usuario)

    guardarUsuario(lista)

def log(accion):
    logg = accion + ", " + datetime.datetime.now().strftime("%c") + "\n"
    with open("log.txt","a",encoding="utf-8") as fichero:
        fichero.write(accion + ", " + datetime.datetime.now().strftime("%c") + "\n")

def guardarUsuario(lista):
    with open("usuarios.csv", "w", encoding="utf-8") as fichero:
        escribir = csv.DictWriter(fichero, fieldnames=CAMPOS)
        escribir.writeheader()
        for l in lista:
            escribir.writerow(l)

def listar(lista):
    log("Listado")
    if not lista:
        print("No hay usuarios")
        return

    for l in lista:
        print("Id: ",l["id"])
        print("Nombre: ",l["nombre"])
        print("Email: ",l["email"])
        print("Edad: ",l["edad"])
        print("Rol: ",l["rol"],"\n")
    
def buscarEmail(lista):
    log("Buscar por email")
    if not lista:
        print("No hay usuarios")
        return
    
    email = input("Email: ").strip()

    for l in lista:
        if(l["email"] == email):
            print("El usuario con email ", email, " es ", l["nombre"])

def eliminar(lista):
    log("Eliminar usuario")

    if not lista:
        print("No hay lista")
        return

    nombre = input("Nombre: ").strip().lower()

    for i in range(len(lista)):
        if lista[i]["nombre"].lower() == nombre:
            lista.pop(i)
            print("Usuario eliminado")
            guardarUsuario(lista)
            return
        
    print("Usuario no encontrado")

def modificarRol(lista):
    log("Modificar rol")

    if not lista:
        print("No hay lista")
        return
    nombre = input("Nombre: ").strip().lower()

    for i in range(len(lista)):
        if lista[i]["nombre"].lower() == nombre:
            rol = input("Rol: ").strip()
            lista[i]["rol"] = rol
            print("Rol de ", lista[i]["nombre"], " cambiado")
            guardarUsuario(lista)
            return
        
    print("Usuario no encontrado")


# -------- Main ---------

while True:
    menu()

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        anadirUsuario(lista)
    elif opcion == "2":
        listar(lista)
    elif opcion == "3":
        buscarEmail(lista)
    elif opcion == "4":
        eliminar(lista)
    elif opcion == "5":
        modificarRol(lista)
    elif opcion == "6":
        print("Saliendo...")
        log("Salir")
        break
    else: 
        print("Opcion no valida")