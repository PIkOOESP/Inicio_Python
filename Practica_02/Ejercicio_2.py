print("Introduce una nota")
x = input()
x = float(x)

if x < 0 :
    print("Resultado falso")
elif x >= 0 and x < 5 :
    print("Suspenso")
elif x >= 5 and x <= 6.9:
    print("Aprovado")
elif x >= 7 and x <= 8.9 :
    print("Notable")
elif x >= 9 and x <= 10:
    print("Sobresaliente")
elif x > 10 :
    print("Resultado falso")