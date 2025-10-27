user = "admin"
passwd = "python123"
contador = 0

while(True):
    print("Introduce el usuario")
    usuario = input()
    
    print("Introduce la contraseña")
    contra = input()
    
    if usuario == user and contra == passwd:
        print("Acceso Permitir")
        break
    else :
        contador += 1
    
    if contador == 3:
        print("Acceso bloqueado")
        break