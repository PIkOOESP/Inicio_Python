class Coche:
    ruedas = 3

    def __init__(self, marca, velocidad, modelo):
        self.marca = marca
        self.velocidad = velocidad
        self.modelo = modelo

    def acelerar(self, cantidad):
        self.velocidad += cantidad

    def frenar(self, cantidad):
        self.velocidad -= cantidad

    def mostrar_estado(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Velocidad: {self.velocidad} km/h, Ruedas: {self.ruedas}")
        