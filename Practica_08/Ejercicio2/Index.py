from Coche import Coche

coche1 = Coche("Toyota", 120, "Corolla")
coche2 = Coche("Honda", 150, "Civic")

coche1.acelerar(30)
coche1.frenar(10)

coche2.acelerar(50)
coche2.frenar(20)

coche1.mostrar_estado()
coche2.mostrar_estado()

print(coche1.ruedas)
print(coche2.ruedas)