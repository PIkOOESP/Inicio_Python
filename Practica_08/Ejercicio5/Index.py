from Libro import Libro

def menu():
    print("Menú de Biblioteca")
    print("Añadir libro")
    print("Listar libros")
    print("Prestar libro")
    print("Devolver libro")
    print("Salir")


while True:
    biblioteca = []
    menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        titulo = input("Título del libro: ").strip()
        autor = input("Autor del libro: ").strip()
        ano_publicacion = int(input("Año de publicación: ").strip())
        estado = "Disponible"
        libro = Libro(titulo, autor, ano_publicacion, estado)
        biblioteca.append(libro)

    elif opcion == "2":
        if not biblioteca:
            print("No hay libros en la biblioteca.")
            break
        
        for libro in biblioteca:
            libro.mostrar_informacion()

    elif opcion == "3":
        if not biblioteca:
            print("No hay libros en la biblioteca.")
            break

        titulo = input("Título del libro a prestar: ").strip()
        for libro in biblioteca:
            if libro.titulo == titulo:
                libro.prestado()
                break

    elif opcion == "4":
        if not biblioteca:
            print("No hay libros en la biblioteca.")
            break
        
        titulo = input("Título del libro a devolver: ").strip()
        for libro in biblioteca:
            if libro.titulo == titulo:
                libro.devuelto()
                break

    elif opcion == "5":
        break