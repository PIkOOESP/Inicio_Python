import time

saldo = 1000
while(True):
    print("Menú de opciones:\n1. Consultar saldo\n2. Ingresar dinero\n3. Retirar dinero\n4. Salir")
    x = input()
    time.sleep(2)

    try:
        x = int(x)  
    except ValueError:
        print("\nDebe introducirse un numero\n")
        time.sleep(2)
        
    if x == 1:
        print("\nSu saldo es de " + str(saldo) + "\n")
        time.sleep(2)
    elif x == 2:
        print("\n¿Cuando dinero quiere ingresar?")
        ingreso = input()
        
        try:
            ingreso = int(ingreso)
            saldo += ingreso
            print("\nDinero ingresado correctamente\n")
            time.sleep(2)
        except ValueError:
            print("\nDebe introducir un numero\n")
            time.sleep(2)
    elif x == 3:
        print("\n¿Cuanto dinero quiere retirar?")
        retirada = input()
        
        try:
            retirada = int(retirada)
            if retirada > saldo:
                print("\nNo se puede retirar mas saldo del que tiene\n")
                time.sleep(2)
            else:
                saldo -= retirada
                print("\nDinero retirado correctamente\n")
                time.sleep(2)
        except ValueError:
            print("\nDebe ser un numero\n")
            time.sleep(2)
    elif x == 4:
        print("Saliendo...")
        break