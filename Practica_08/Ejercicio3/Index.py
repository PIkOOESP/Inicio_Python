from CuentaBancaria import CuentaBancaria

cuenta1 = CuentaBancaria("Juan", 1000)

cuenta1.ingresar(500)
cuenta1.retirar(200)
cuenta1.retirar(2000)  # Intento de retiro con fondos insuficientes
print("Saldo actual:", cuenta1.mostrar_saldo())
print("Movimientos realizados:", cuenta1.mostrar_movimientos())