class Usuario:
    total_usuarios = 0

    def __init__(self, nombre):
        self.nombre = nombre
        Usuario.total_usuarios += 1

    def mostrar_nombre(self):
        return f"Hola, mi nombre es {self.nombre}."
    
    @classmethod
    def mostrar_total(cls):
        return f"Total de usuarios: {cls.total_usuarios}"
    
    @staticmethod
    def validar_nombre(nombre):
        return len(nombre) > 3