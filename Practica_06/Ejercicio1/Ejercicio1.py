"""
Programa de gestion de notas en ficheros
"""

# ----------- Funciones -----------

def menu():
    print("=====MENU=====")
    print("1. Añadir una nueva nota")
    print("2. Mostrar todas las notas")
    print("3. Buscar una asignatura y mostrar su nota")
    print("4. Media de todas las notas")
    
    
def anadirNota():
    asignatura = input("Asignatura: ").strip()
    nota = input("Nota: ").strip()
    with open("notas.txt", "a", encoding="utf-8") as fichero:
        fichero.write(asignatura,"-",nota)
    
def mostrarNotas():
    with open("notas.txt", "r", encoding="utf-8") as fichero:
        notas = fichero.readline()
        for n in notas:
            print(n)
            
def buscarAsignatura():
    asignatura = input("Asignatura: ").strip()
    
    with open("notas.txt", "r", encoding="utf-8") as fichero:
        notas = fichero.readline()
        asignaturas = []
        for n in notas:
            asignaturas.push(n.split("-"))
        
        for i in range(len(asignaturas)):
            if(asignaturas[i] == asignatura):
                print("Asignatura: ", asignaturas[i], "\nNota: ", asignaturas[i+1])
                return
            
        print("Asignatura no encontrada")
        
def sumarNotas():
        