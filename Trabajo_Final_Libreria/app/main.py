"""
Programa de gestion de usuarios, bibliotecarios y libros de una biblioteca
"""

def main():
    

    while True:
        menu()
        opcion = input("Elige una opcion:").strip()
        
        if opcion == "1":
            while True:
                menu_usuarios()
                opcion2 = input("Elige una opcion:").strip()
                if opcion2 == "1":
                    crearUsuario()
                    
                elif opcion2 == "2":
                    borrarUsuario()
                    
                elif opcion2 == "3":
                    buscarUsuario()
                    
                elif opcion2 == "4":
                    modificarUsuario()
                    
                elif opcion2 == "5":
                    break
                
                else:
                    print("Elige una opción válida")
        
        elif opcion == "2":
            while True:
                menu_libros()
                opcion2 = input("Elige una opción:").strip()
                if opcion2 == "1":
                    crearLibro()
                    
                elif opcion2 == "2":
                    borrarLibro()
                    
                elif opcion2 == "3":
                    buscarLibro()
                    
                elif opcion2 == "4":
                    modificarLibro()
                    
                elif opcion2 == "5":
                    break
                    
                else:
                    print("Elige una opción válida")

        elif opcion == "3":
            print("Saliendo del programa...")
            break
    
def menu():
    print("---Menú Biblioteca---")
    print("1.Usuarios.")
    print("2.Libros.")
    print("3.Salir.")
    
def menu_usuarios():
    print("---Menu de gestion de usuarios---")
    print("1.Añadir usuario")
    print("2.Borrar usuario")
    print("3.Buscar usuario")
    print("4.Modificar usuario")
    print("5.Salir")
    
def menu_libros():
    print("---Menu de gestion de libros---")
    print("1.Añadir libros")
    print("2.Borrar libros")
    print("3.Buscar libros")
    print("4.Modificar libros")
    print("5.Salir")