
class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def saludar(self):
        print("Hola, me llamo ", self.nombre)
        
    def es_mayor_edad(self):
        if self.edad >= 18:
            print(self.nombre," es mayor de edad.")
        else:
            print(self.nombre," no es mayor de edad.")