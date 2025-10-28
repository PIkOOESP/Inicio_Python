# ================================
# GESTOR DE NOTAS (versión simple)
# ================================

"""
Este programa permite gestionar alumnos y sus notas.
Cada alumno se almacena en un diccionario dentro de una lista.
Incluye funciones, estructuras de control y conceptos de mutabilidad.
"""

# ---------- FUNCIONES ----------

def menu():
    """Muestra el menú principal."""
    print("\n=== GESTOR DE NOTAS ===")
    print("1. Añadir alumno")
    print("2. Mostrar todos los alumnos")
    print("3. Gestionar nota a un alumno")
    print("4. Mostrar notas y promedio de un alumno")
    print("5. Estadísticas generales")
    print("6. Eliminar un alumno")
    print("7. Ranking de alumnos")
    print("8. Salir")

# Ejercicio 3
def menu_notas(nombre):
    """Muestra el menú para gestionar las notas de un alumno"""
    print("\n===GESTOR DE NOTAS DE " + nombre.upper() + "===")
    print("1. Añadir nota")
    print("2. Editar nota")
    print("3. Eliminar nota")
    print("4. Salir")

# Ejercicio 5
def menu_informe():
    """Muestra el menú para elegir el informe"""
    print("\n===INFORMES===")
    print("1. Media de un alumno")
    print("2. Mediana de un alumno")
    print("3. Mejor y peor nota de un alumno")
    print("4. Media global")
    print("5. Desviacion estandar")
    print("6. Varianza")
    print("7. Distribucion por tramos")
    print("8. Alumnos en riesgo")
    print("9. Salir")

def crear_alumno(nombre, edad, trabaja=False):
    """Crea un diccionario con los datos del alumno."""
    return {"nombre": nombre, "edad": edad, "trabaja": trabaja, "notas": []}

def mostrar_alumnos(lista):
    """Muestra el nombre y la edad de cada alumno."""
    if not lista:
        print("No hay alumnos registrados.")
        return
    print("\nListado de alumnos:")
    for i, alumno in enumerate(lista):
        print(f"{i+1}. {alumno['nombre']} ({alumno['edad']} años)")

def buscar_alumno(lista, nombre):
    """Devuelve el índice de un alumno por nombre (o None si no existe)."""
    for i, alumno in enumerate(lista):
        if alumno["nombre"].lower() == nombre.lower():
            return i
    return None

# Ejercicio 3
def anadir_nota(lista, i):
    """Una nota, y la añade."""
    try:
        nota = float(input("Introduce la nota (0-10): "))
        if 0 <= nota <= 10:
            lista[i]["notas"].append(nota)
            print("Nota añadida correctamente.")
        else:
            print("La nota debe estar entre 0 y 10.")
    except ValueError:
        print("Debes introducir un número.")

# Ejercicio 3
def editar_nota(lista,i):
    """Pide una nota y la edita"""
    try:
        for e in range(len(lista[i]["notas"])):
            print (str(e) + ": " + str(lista[i]["notas"][e]))

        opcion = int(input("Introduce la posicion de la nota que quieres\n"))
        lista[i]["notas"][opcion] = input("Introduce la nota deseada\n")
    except ValueError:
        print("Debe ser un numero de la lista")
    except IndexError:
        print("El numero debe estar en la lista")

# Ejercicio 3
def eliminar_nota(lista,i):
    try:
        opcion = int(input("Introduce la posicion de la nota que quieres"))
        lista[i]["notas"].pop(opcion)
    except ValueError:
        print("Debe ser un numero de la lista")

def mostrar_notas(lista):
    """Muestra las notas de un alumno concreto."""
    nombre = input("Nombre del alumno: ")
    i = buscar_alumno(lista, nombre)
    if i is None:
        print("Alumno no encontrado.")
        return
    notas = lista[i]["notas"]
    if not notas:
        print("Este alumno no tiene notas aún.")
        return
    promedio = sum(notas) / len(notas)
    print(f"Notas de {nombre}: {notas}")
    print(f"Promedio: {promedio:.2f}")

def estadisticas(lista):
    """Calcula datos generales del grupo."""
    if not lista:
        print("No hay alumnos registrados.")
        return
    total_notas = [n for alumno in lista for n in alumno["notas"]]
    if not total_notas:
        print("Ningún alumno tiene notas aún.")
        return

    media_general = sum(total_notas) / len(total_notas)
    mayor_edad = max(lista, key=lambda x: x["edad"])
    print(f"Media general del grupo: {media_general:.2f}")
    print(f"Alumno de mayor edad: {mayor_edad['nombre']} ({mayor_edad['edad']} años)")

    # Contar cuántos trabajan (ejemplo booleano)
    trabajan = [a for a in lista if a["trabaja"]]
    print(f"Alumnos que trabajan: {len(trabajan)} / {len(lista)}")
    
# Ejercicio 1    
def eliminar_alumno(lista):
    """Elimina un alumno por nombre"""
    nombre = input("Nombre del alumno: ").strip()
    i = buscar_alumno(lista, nombre)
    if i is None:
        print("Alumno no encontrado")
        return
    else:
        opcion = input("Estas seguro que deseas eliminar al alumno :" + nombre + "\n")
        if opcion in ("si", "sí", "yes", "y"):
            lista.pop(i)
            print("Alumno borrado correctamente")
        else :
            print("No se ha borrado al alumno")

# Ejercicio 2
def editar_alumno(lista):
    """Edita todos los campos de alumno"""
    nombre = input("Nombre del alumno: ").strip()
    i = buscar_alumno(lista, nombre)
    if i is None:
        print("Alumno no encontrado")
        return
    else:
        opcion = input("¿Quieres editar el nombre?")
        if opcion in ("si", "sí", "yes", "y"):
            lista[i]["nombre"] = input("Introduce el nombre")
            
        opcion = input("¿Quieres editar la edad?")
        if opcion in ("si", "sí", "yes", "y"):
            lista[i]["edad"] = input("Introduce la edad")
        
        opcion = input("¿Trabaja?").lower()
        if opcion in ("si", "sí", "yes", "y"):
            lista[i]["trabaja"] = True
        elif opcion in ("no", "n"):
            lista[i]["trabaja"] = False
        
# Ejercicio 3
def gestionar_notas(lista):
    """Gestiona las notas de un alumno"""
    nombre = input("Nombre del alumno: ").strip()
    i = buscar_alumno(lista,nombre)
    if i is None:
        print("Alumno no encontrado")
        return
    while True:
        menu_notas(nombre)
        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            anadir_nota(lista, i)
        elif opcion == "2":
            editar_nota(lista, i)
        elif opcion == "3":
            eliminar_nota(lista, i)
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejercicio 4
def ranking(lista):
    """Muestra una lista con el promedio de notas de los alumnos"""
    if(len(lista) == 0):
        print("No hay alumnos")
        return

    lista_desordenada = []
    contador = 0
    for i in range(len(lista)):
        if len(lista[i]["notas"]) == 0:
            continue
        notas ={"nombre" : lista[i]["nombre"] , "media" : (sum(lista[i]["notas"]) / len(lista[i]["notas"]))}
        lista_desordenada.append(notas)

    lista_ordenada = sorted(lista_desordenada, key=lambda x: x["media"], reverse=True)

    for i in range(len(lista_ordenada)):
        print(lista_ordenada[i]["nombre"] + " nota media: " + str(lista_ordenada[i]["media"]), end=" ")
        if lista_ordenada[i]["media"] < 5 :
            print("Suspenso")
        elif lista_ordenada[i]["media"] >= 5 and lista_ordenada[i]["media"] <= 6 :
            print("Aprobado")
        elif lista_ordenada[i]["media"] >= 7 and lista_ordenada[i]["media"] <= 8 :
            print("Notable")
        else :
            print("Sobresaliente")

#Ejercicio 5
def informe(lista):
    """Muestra un informe extenso con los datos de los alumnos"""

 
# ---------- PROGRAMA PRINCIPAL ----------

alumnos = []

while True:
    menu()
    opcion = input("Selecciona una opción: ").strip()

    if opcion == "1":
        nombre = input("Nombre: ").strip().title()
        edad = int(input("Edad: "))
        trabaja_input = input("¿Trabaja? (si/no): ").lower()
        trabaja = trabaja_input in ("si", "sí", "yes", "y")
        alumno = crear_alumno(nombre, edad, trabaja)
        alumnos.append(alumno)
        print(f"Alumno {nombre} añadido correctamente.")

    elif opcion == "2":
        mostrar_alumnos(alumnos)

    elif opcion == "3":
        gestionar_notas(alumnos)

    elif opcion == "4":
        mostrar_notas(alumnos)

    elif opcion == "5":
        estadisticas(alumnos)
    
    elif opcion == "6":
        eliminar_alumno(alumnos)

    elif opcion == "7":
        ranking(alumnos)

    elif opcion == "8":
        print("Fin del programa. ¡Hasta la próxima!")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")
