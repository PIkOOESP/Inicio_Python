class CuentaBancaria:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo
        self.movimientos = []

    def ingresar(self,cantidad):
        self.saldo += cantidad
        self.movimientos.append(("ingreso", cantidad))

    def retirar(self,cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            self.movimientos.append(("retiro", cantidad))
        else:
            print("Fondos insuficientes")

    def mostrar_saldo(self):
        return self.saldo
    
    def mostrar_movimientos(self):
        return self.movimientos 