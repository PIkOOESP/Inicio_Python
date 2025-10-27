usuario = "admin"
contraseña = "1234"

print("Introduce el usuario")
nombre = input()

print("Introduce la contraseña")
passwd = input()

if usuario == nombre and contraseña == passwd :
    print("Acceso permitido")
else :
    print("Acceso denegado")