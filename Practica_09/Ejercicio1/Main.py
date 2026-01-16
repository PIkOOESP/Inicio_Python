from Usuario import Usuario

usuario1 = Usuario("Ana")
usuario2 = Usuario("Luis")

print(usuario1.mostrar_nombre())
print(usuario2.mostrar_nombre())
print(Usuario.mostrar_total())
print(Usuario.validar_nombre(usuario1.nombre))
print(Usuario.validar_nombre(usuario2.nombre))
