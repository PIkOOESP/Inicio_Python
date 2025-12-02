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
    print("5. Salir")
    
def anadirNota():
    asignatura = input("Asignatura: ").strip()
    nota = input("Nota: ").strip()
    with open("notas.txt", "a", encoding="utf-8") as fichero:
        fichero.write(asignatura + "-" + nota + "\n")
    
def mostrarNotas():
    with open("notas.txt", "r", encoding="utf-8") as fichero:
        notas = fichero.readlines()
        for n in notas:
            print(n)
            
def buscarAsignatura():
    asignatura = input("Asignatura: ").strip()
    
    with open("notas.txt", "r", encoding="utf-8") as fichero:
        notas = fichero.readlines()
        asignaturas = []
        for i in range(len(notas)):
            asignaturas.append(notas[i].split("-"))
        
        for i in range(len(asignaturas)):
            for a in range(len(asignaturas[i])):
                if(asignaturas[i][a] == asignatura):
                    print("Asignatura: ", asignaturas[i][a], "\nNota: ", asignaturas[i][a+1])
                    return
            
        print("Asignatura no encontrada")
        
def sumarNotas():
    with open("notas.txt","r", encoding="utf-8") as fichero:
        notas = fichero.readlines()
        nota = []
        total = 0
        for n in notas:
            nota.append(n.split("-"))
            
        for i in range(len(nota)):
            for a in range(len(nota[i])):
                try:
                    total += float(nota[i][a])
                except ValueError:
                    None
        
        print("Suma de todas las notas: ", total)



# ----------- Programa principal -----------
while True:
    menu()

    opcion = input("Opcion: ").strip()

    if opcion == "1":
        anadirNota()
    elif opcion == "2":
        mostrarNotas()
    elif opcion == "3":
        buscarAsignatura()
    elif opcion == "4":
        sumarNotas()
    elif opcion == "5":
        print("Saliendo...")
        break
    else:
        print("Opcion no valida")