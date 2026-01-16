class Libro:
    def __init__(self, titulo, autor, ano_publicacion, estado):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacion = ano_publicacion
        self.estado = estado


    def mostrar_informacion(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de Publicación: {self.ano_publicacion}")
        print(f"Estado: {self.estado}")

    def prestado(self):
        self.estado = "Prestado"
        print(f"El estado del libro '{self.titulo}' ha sido cambiado a '{self.estado}'.")

    def devuelto(self):
        self.estado = "Disponible"
        print(f"El estado del libro '{self.titulo}' ha sido cambiado a '{self.estado}'.")