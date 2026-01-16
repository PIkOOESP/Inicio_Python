from Alumno import Alumno

alumno1 = Alumno("Ana", 20, 7.5)
alumno2 = Alumno("Luis", 22, 4.3)
alumno3 = Alumno("Marta", 19, 5.0)

alumnos = [alumno1, alumno2, alumno3]

for alumno in alumnos:
    print(alumno.mostrar_informacion())