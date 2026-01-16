class Motor:
    def arrancar(self):
        return "Motor encendido."

class Radio:
    def encender_radio(self):
        return "Radio encendida."

class Coche(Motor, Radio):
    def arrancar(self):
        return super().arrancar() + " - Sistema moderno listo."