"""
Modelo de la clase Persona.

Modelo de la clase Usuario, que extiende de Persona.

Modelo de la clase Bibliotecario, que extiende de Persona.
"""

import re

class Persona:
    cantidad_personas = 0 
    
    def __init__(self, nombre, apellido, dni, edad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__edad = edad
        Persona.cantidad_personas += 1
        
    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getDni(self):
        return self.__dni
    
    def getEdad(self):
        return self.__edad
    
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def setApellido(self, apellido):
        self.__apellido = apellido
        
    def setDni(self, dni):
        self.__dni = dni
        
    def setEdad(self, edad):
        self.__edad = edad
        
    def mostrar_info(self):
        return f"Nombre:{self.__nombre}\nApellido:{self.__apellido}\nDni:{self.__dni}\nEdad:{self.__edad}"
    
    @classmethod
    def mostrar_total(cls):
        return f"Total de personas: {cls.cantidad_personas}"
    
    @staticmethod
    def validar_dni(dni):
        return bool(re.match(r'^\d{8}[a-zA-Z]{1}$', dni))
        
class Usuario(Persona):
    cantidad_usuarios = 0
    
    def __init__(self, nombre, apellido, dni, edad, email):
        super().__init__(nombre, apellido, dni, edad)
        self.__email = email
        Usuario.cantidad_usuarios += 1
        
    def getEmail(self):
        return self.__email
    
    def setEmail(self, email):
        self.__email = email
        
    def mostrar_info(self):
        info_persona = super().mostrar_info()
        return f"{info_persona}\nEmail:{self.__email}"
    
    @classmethod
    def mostrar_total(cls):
        return f"Total de personas: {cls.cantidad_usuarios}"