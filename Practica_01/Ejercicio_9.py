print("Introduce la primera nota")
x = input()
x = int(x)

print("Introduce la segunda nota")
y = input()
y = int(y)

print("Introduce la tercera nota")
z = input()
z = int(z)

resultado = (x + y + z) / 3
if resultado < 0 :
    print("Resultado falso")
elif resultado >= 0 and resultado < 5 :
    print("Suspenso")
elif resultado >= 5 and resultado <= 6:
    print("Aprovado")
elif resultado > 6 and resultado < 9 :
    print("Notable")
elif resultado >= 9 and resultado <= 10:
    print("Sobresaliente")
elif resultado > 10 :
    print("Resultado falso")