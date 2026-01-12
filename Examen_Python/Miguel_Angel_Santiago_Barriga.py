"""
Esto es un programa de gestion de cursos e inscripciones de alumnos
"""
# -------- Funciones --------

def menu():
    """ Enseña el menú principal """
    print("=====GESTOR DE CURSOS======")
    print("1. Añadir curso")
    print("2. Mostrar cursos")
    print("3. Cambiar estado del curso")
    print("4. Resumen de actividad")
    print("5. Salir...")
    
def crear_curso(nombre, profesor, horas, plazas):
    """ Crea el diccionario curso """
    curso = {"nombre" : nombre , "profesor" : profesor, "horas" : horas, "plazas" : plazas, "estado" : "Abierto"}
    return curso

def buscar_curso(lista, nombre):
    """ Busca un curso y devuelve su indice en la lista, si no lo encuentra devuelve None """
    for i in range(len(lista)):
        if lista[i]["nombre"] == nombre :
            return i
        
    return None

def mostrar(lista):
    """ Muestra una lista de todos los cursos """
    if not lista:
        print("\n No hay cursos \n")
    
    for i in range(len(lista)):
        print(str(i+1) + ". Nombre del curso: " + lista[i]["nombre"])
        print("Profesor: " + lista[i]["profesor"])
        print("Horas lectivas: " + str(lista[i]["horas"]))
        print("Plazas disponibles: " + str(lista[i]["plazas"]))
        print("Estado: " + lista[i]["estado"] + "\n\n")
        
def cambiar_estado(lista):
    """ Cambia el estado de un curso concreto s"""
    if not lista:
        print("\n No hay cursos \n")
    
    nombre = input("Nombre del curso: ").strip()
    i = buscar_curso(lista, nombre)
    
    if i is None:
        print("Curso no encontrado")
        return
    
    print("-- Estados --")
    print("1. Abierto")
    print("2. En progreso")
    print("3. Cerrado") 
    print("4. Cancelado")
    
    while True:
        try:
            estado = int(input("Opcion: "))
            
            if estado == 1 :
                lista[i]["estado"] = "Abierto"
                break
            elif estado == 2 :
                lista[i]["estado"] = "En progreso"
                break
            elif estado == 3 :
                lista[i]["estado"] = "Cerrado"
                break
            elif estado == 4 :
                lista[i]["estado"] = "Cancelado"
                break
            else : 
                print("Introduzca una opcion válida.")
        except ValueError:
            print("Debe ser un numero entero")
            
def resumen(lista):
    """ Muestra un resumen de todos los datos de los cursos """
    total = len(lista)
    plazas_totales = 0
    abierto = 0
    cerrado = 0
    progreso = 0
    cancelado = 0
    print("Numero total de cursos: " + str(total))
    
    for i in range(len(lista)):
        if lista[i]["estado"] == "Abierto":
            abierto += 1
            
        if lista[i]["estado"] == "Cerrado" :
            cerrado += 1
            
        if lista[i]["estado"] == "En progreso" :
            progreso += 1
            
        if lista[i]["estado"] == "Cancelado" :
            cancelado += 1
            
        plazas_totales += lista[i]["plazas"]
    
    porcentaje = cerrado * 100/total
        
    print("Cursos abiertos: " + str(abierto))
    print("Cursos cerrados: " + str(cerrado))
    print("Cursos en progreso: " + str(progreso))
    print("Cursos cancelados: " + str(cancelado))
    print("Plazas totales ofertadas: " + str(plazas_totales))
    print("Porcentaje de cursos cerrados: " + str(porcentaje) + "%")
    
    
    
# -------- Programa principal --------
cursos = []

while True:
    menu()
    opcion = input("Opcion: ").strip()
    
    if opcion == "1":
        nombre = input("Nombre del curso: ").strip()
        profesor = input("Nombre del profesor: ").strip()
        
        while True:
            try:
                horas = int(input("Numero de horas: "))
                
                if horas < 0 : 
                    print("Debe ser un numero positivo")
                else:
                    break
            except ValueError:
                print("Debe ser un numero")
                
        while True:
            try:
                plazas = int(input("Numero de plazas: "))
                
                if plazas < 0 : 
                    print("Debe ser un numero positivo")
                else:
                    break
            except ValueError:
                print("Debe ser un numero")
                
        curso = crear_curso(nombre, profesor, horas, plazas)
        cursos.append(curso)
    elif opcion == "2":
        mostrar(cursos)
    
    elif opcion == "3":
        cambiar_estado(cursos)
        
    elif opcion == "4":
        resumen(cursos)                
              
    elif opcion == "5":
        break
    
    else :
        print("Debe introducir una opcion válida")  
