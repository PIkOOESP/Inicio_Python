class Alumno:
    def __init__(self, nombre,edad, nota_media):
        self.nombre = nombre
        self.edad = edad
        self.nota_media = nota_media

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Nota Media: {self.nota_media}, Aprobado: {'Sí' if self.aprobado() else 'No'}"
    
    def aprobado(self):
        return self.nota_media >= 5