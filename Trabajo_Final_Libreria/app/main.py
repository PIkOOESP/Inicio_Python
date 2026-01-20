from models.persona import Persona, Usuario
from models.libro import Libro
import os
import csv

"""
Programa de gestion de usuarios y libros de una libreria
"""

# Esta direccion se debe cambiar si el programa no funciona
os.chdir(os.getcwd()+ "/Inicio_Python/Trabajo_Final_Libreria/app/data")

libros = []
usuarios = []

def inicializarSistema(usuarios, libros):
    """Funcionalidad para inicializar el sistema"""
    print("Inicializando el sistema de gestión de biblioteca...")

    try:
        with open("usuarios.csv", "x") as f:
            pass  
    except FileExistsError:
        pass  

    try:
        with open("libros.csv", "x") as f:
            pass
    except FileExistsError:
        pass

    with open("usuarios.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            usuario = Usuario(row["nombre"], row["apellido"], row["dni"], row["edad"], row["email"])
            usuarios.append(usuario)
    print(f"Cargados {len(usuarios)} usuarios.")
    
    with open("libros.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            libro = Libro(row["titulo"], row["autor"], row["isbn"], row["editorial"])
            libros.append(libro)
    print(f"Cargados {len(libros)} libros.")
        
    print("Sistema inicializado con éxito.")

def main(usuarios, libros):
    """Funcionalidad principal del programa"""
    inicializarSistema(usuarios, libros)
    while True:
        menu()
        opcion = input("Elige una opcion:").strip()
        
        if opcion == "1":
            while True:
                menu_usuarios()
                opcion2 = input("Elige una opcion:").strip()
                if opcion2 == "1":
                    crearUsuario(usuarios)
                    
                elif opcion2 == "2":
                    borrarUsuario(usuarios)
                    
                elif opcion2 == "3":
                    buscarUsuario(usuarios)
                    
                elif opcion2 == "4":
                    modificarUsuario(usuarios)

                elif opcion2 == "5":
                    listarUsuarios(usuarios)

                elif opcion2 == "6":
                    guardarUsuarios(usuarios)
                    
                elif opcion2 == "7":
                    print("Saliendo del menú de usuarios...")
                    break
                
                else:
                    print("Elige una opción válida")
        
        elif opcion == "2":
            while True:
                menu_libros()
                opcion2 = input("Elige una opción:").strip()
                if opcion2 == "1":
                    crearlibro(libros)
                    
                elif opcion2 == "2":
                    borrarLibro(libros)
                    
                elif opcion2 == "3":
                    buscarLibro(libros)
                    
                elif opcion2 == "4":
                    modificarLibro(libros)

                elif opcion2 == "5":
                    venderLibro(libros, usuarios)

                elif opcion2 == "6":
                    listarLibros(libros)

                elif opcion2 == "7":
                    guardarLibros(libros)
                    
                elif opcion2 == "8":
                    print("Saliendo del menú de libros...")
                    break
                    
                else:
                    print("Elige una opción válida")

        elif opcion == "3":
            print("Saliendo del programa...")
            break
    
def menu():
    """Menu principal del programa"""
    print("---Menú Biblioteca---")
    print("1.Usuarios.")
    print("2.Libros.")
    print("3.Salir.")
    
def menu_usuarios():
    """Menu de gestion de usuarios"""
    print("---Menu de gestion de usuarios---")
    print("1.Añadir usuario")
    print("2.Borrar usuario")
    print("3.Buscar usuario")
    print("4.Modificar usuario")
    print("5.Listar usuarios")
    print("6.Guardar usuarios")
    print("7.Salir")

def menu_libros():
    """Menu de gestion de libros"""
    print("---Menu de gestion de libros---")
    print("1.Añadir libros")
    print("2.Borrar libros")
    print("3.Buscar libros")
    print("4.Modificar libros")
    print("5.Vender libros")
    print("6.Listar libros")
    print("7.Guardar libros")
    print("8.Salir")

def crearUsuario(lista):
    """Funcionalidad para crear usuario"""

    nombre = input("Introduce el nombre del usuario: ").strip()
    apellido = input("Introduce el apellido del usuario: ").strip()
    
    while True:
        dni = input("Introduce el DNI del usuario: ").strip()
        if Persona.validar_dni(dni):
            break
        else:
            print("DNI inválido. Debe tener 8 dígitos seguidos de una letra.")
        
    edad = input("Introduce la edad del usuario: ").strip()
    email = input("Introduce el email del usuario: ").strip()
    usuario = Usuario(nombre, apellido, dni, edad, email)
    print("Usuario creado con éxito:")
    print(usuario.mostrar_info())
    lista.append(usuario)

def borrarUsuario(lista):
    """Funcionalidad para borrar usuario"""
    if not lista:
        print("No hay usuarios.")
        return

    dni = input("Introduce el DNI del usuario a borrar: ").strip()
    for usuario in lista:
        if usuario.getDni() == dni:
            lista.remove(usuario)
            print("Usuario borrado con éxito.")
            return
    print("Usuario no encontrado.")

def buscarUsuario(lista):
    """Funcionalidad para buscar usuario"""
    if not lista:
        print("No hay usuarios.")
        return

    dni = input("Introduce el DNI del usuario a buscar: ").strip()
    for usuario in lista:
        if usuario.getDni() == dni:
            print("Usuario encontrado:")
            print(usuario.mostrar_info())
            return
    print("Usuario no encontrado.")

def modificarUsuario(lista):
    """Funcionalidad para modificar usuario"""
    if not lista:
        print("No hay usuarios.")
        return

    dni = input("Introduce el DNI del usuario a modificar: ").strip()
    for usuario in lista:
        if usuario.getDni() == dni:
            print("Usuario encontrado. Introduce los nuevos datos:")
            nombre = input("Nuevo nombre (deja en blanco para no cambiar): ").strip()
            apellido = input("Nuevo apellido (deja en blanco para no cambiar): ").strip()
            edad = input("Nueva edad (deja en blanco para no cambiar): ").strip()
            email = input("Nuevo email (deja en blanco para no cambiar): ").strip()
            
            if nombre:
                usuario.setNombre(nombre)
            if apellido:
                usuario.setApellido(apellido)
            if edad:
                usuario.setEdad(edad)
            if email:
                usuario.setEmail(email)
                
            print("Usuario modificado con éxito:")
            print(usuario.mostrar_info())
            return
    print("Usuario no encontrado.")


def listarUsuarios(lista):
    """Funcionalidad para listar usuarios"""
    if not lista:
        print("No hay usuarios.")
        return

    print("Lista de usuarios:")
    for usuario in lista:
        print(usuario.mostrar_info())
        print("-----")

def guardarUsuarios(lista):
    """Funcionalidad para guardar usuarios en un archivo"""

    with open("usuarios.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=["nombre", "apellido", "dni", "edad", "email"])
        writer.writeheader()
        for usuario in lista:
            writer.writerow({
                "nombre": usuario.getNombre(),
                "apellido": usuario.getApellido(),
                "dni": usuario.getDni(),
                "edad": usuario.getEdad(),
                "email": usuario.getEmail()
            })
    print("Usuarios guardados con éxito en 'usuarios.csv'.")

def crearlibro(lista):
    """Funcionalidad para crear libro"""

    titulo = input("Introduce el título del libro: ").strip()
    while True:
        isbn = input("Introduce el ISBN del libro: ").strip()
        if Libro.es_isbn_valido(isbn):
            break

        print("ISBN inválido. Debe seguir el formato 978-84-XXXX-XXXX-X o 979-84-XXXX-XXXX-X.")

    autor = input("Introduce el autor del libro: ").strip()
    editorial = input("Introduce la editorial del libro: ").strip()
    libro = Libro(titulo, isbn, autor, editorial)
    print("Libro creado con éxito:")
    print(libro.mostrar_info())
    lista.append(libro)

def borrarLibro(lista):
    """Funcionalidad para borrar libro"""
    if not lista:
        print("No hay libros.")
        return

    isbn = input("Introduce el ISBN del libro a borrar: ").strip()
    for libro in lista:
        if libro.getIsbn() == isbn:
            lista.remove(libro)
            print("Libro borrado con éxito.")
            return
    print("Libro no encontrado.")

def buscarLibro(lista):
    """Funcionalidad para buscar libro"""
    if not lista:
        print("No hay libros.")
        return

    isbn = input("Introduce el ISBN del libro a buscar: ").strip()
    for libro in lista:
        if libro.getIsbn() == isbn:
            print("Libro encontrado:")
            print(libro.mostrar_info())
            return
    print("Libro no encontrado.")

def modificarLibro(lista):
    """Funcionalidad para modificar libro"""
    if not lista:
        print("No hay libros.")
        return

    isbn = input("Introduce el ISBN del libro a modificar: ").strip()
    for libro in lista:
        if libro.getIsbn() == isbn:
            print("Libro encontrado. Introduce los nuevos datos:")
            titulo = input("Nuevo título (deja en blanco para no cambiar): ").strip()
            autor = input("Nuevo autor (deja en blanco para no cambiar): ").strip()
            editorial = input("Nueva editorial (deja en blanco para no cambiar): ").strip()
            
            if titulo:
                libro.setTitulo(titulo)
            if autor:
                libro.setAutor(autor)
            if editorial:
                libro.setEditorial(editorial)
                
            print("Libro modificado con éxito:")
            print(libro.mostrar_info())
            return
    print("Libro no encontrado.")

def listarLibros(lista):
    """Funcionalidad para listar libros"""
    if not lista:
        print("No hay libros.")
        return

    print("Lista de libros:")
    for libro in lista:
        print(libro.mostrar_info())
        print("-----")

def guardarLibros(lista):
    """Funcionalidad para guardar libros en un archivo"""

    with open("libros.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=["titulo", "isbn", "autor", "editorial"])
        writer.writeheader()
        for libro in lista:
            writer.writerow({
                "titulo": libro.getTitulo(),
                "isbn": libro.getIsbn(),
                "autor": libro.getAutor(),
                "editorial": libro.getEditorial()
            })
    print("Libros guardados con éxito en 'libros.csv'.")

def venderLibro(libros, usuarios):
    """Funcionalidad para vender libro a un usuario"""
    if not libros:
        print("No hay libros disponibles para la venta.")
        return
    if not usuarios:
        print("No hay usuarios registrados para realizar la venta.")
        return

    isbn = input("Introduce el ISBN del libro a vender: ").strip()
    libro_a_vender = None
    for libro in libros:
        if libro.getIsbn() == isbn:
            libro_a_vender = libro
            break

    if not libro_a_vender:
        print("Libro no encontrado.")
        return

    dni = input("Introduce el DNI del usuario que compra el libro: ").strip()
    usuario_comprador = None
    for usuario in usuarios:
        if usuario.getDni() == dni:
            usuario_comprador = usuario
            break
    if not usuario_comprador:
        print("Usuario no encontrado.")
        return

    print(f"Libro '{libro_a_vender.getTitulo()}' vendido a {usuario_comprador.getNombre()} {usuario_comprador.getApellido()}.")
    logVenta(libro_a_vender, usuario_comprador)

    libros.remove(libro_a_vender)

def logVenta(libro, usuario):
    with open("ventas.log", "a") as f:
        f.write(f"Libro '{libro.getTitulo()}' (ISBN: {libro.getIsbn()}) vendido a {usuario.getNombre()} {usuario.getApellido()} (DNI: {usuario.getDni()})\n")

main(usuarios, libros)