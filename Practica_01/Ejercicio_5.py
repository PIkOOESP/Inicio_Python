print("Introduce el primer numero")
x = input()
x = int(x)
lista = [x]

while len(lista) < 5 :
    print("Introduce otro numero")
    x = input()
    x = int(x)
    lista.append(x)

lista = tuple(lista)

#lista[2] = 5 --> Esta linea provoca un fallo ya que no se pueden modificar los elementos de una tupla una vez creada

print(lista)