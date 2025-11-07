# ================================
# Control de productos (versión simple)
# =====================================

"""
Este programa pretende crear un control de una tienda de informatica.
Cada producto se guarda en un diccionario, que a su vez, se guarda en una lista
Incluye funciones, estructuras de control y conceptos de mutabilidad.
"""

# --------- Funciones --------- #

def menu():
    """Muestra el menú principal."""
    print("\n=== GESTOR DE PRODUCTOS ===")
    print("1. Añadir producto")
    print("2. Mostrar todos los productos")
    print("3. Vender un producto")
    print("4. Aplicar descuento")
    print("5. Valor del inventario")
    print("6. Salir")

def crear_producto(nombre, precio, cantidad):
    """Crea un diccionario de un producto"""
    return {"nombre" : nombre, "precio" : precio, "cantidad" : cantidad}

def mostrar_lista(inventario):
    """Muestra todo el inventario"""
    if not inventario:
        print("No hay productos registrados.")
        return
    for i in range (len(inventario)):
            print("Nombre: " + inventario[i]["nombre"] + "\nPrecio: " + str(inventario[i]["precio"]) + "\nCantidad: " + str(inventario[i]["cantidad"]) + "\n\n")

def vender_producto(inventario):
    """Crea una venta de un producto, disminuyendo su stock si es posible y elimina el producto si el stock es 0"""
    if not inventario:
        print("No hay productos registrados.")
        return
    
    seleccion = input("Nombre del producto: ").strip().lower()
    indice = -1
    for i in range(len(inventario)):
        if inventario[i]["nombre"] == seleccion:
            indice = i 
            break

    if indice == -1:
        print ("Producto no encontrado.")
        return
    
    while True:
        try:
            stock = int(input("Nº de productos: ").strip())
            break
        except ValueError:
            print("Debe ser un numero entero\n")

    if stock > inventario[indice]["cantidad"]:
        print("No hay suficiente producto.\n")

    elif stock <= inventario[indice]["cantidad"]:
        print ("Vendidos " + str(stock) + ", " + inventario[indice]["nombre"] + " por la cantidad de " + str(inventario[indice]["cantidad"] * inventario[indice]["precio"]) + "€")
        
        if stock == inventario[indice]["cantidad"]:
            inventario.pop(indice)
        elif stock < inventario[indice]["cantidad"]:
            inventario[indice]["cantidad"] -= stock

def descuento(inventario):
    """Aplica un descuento a todos los productos"""
    if not inventario:
        print("No hay productos registrados.")
        return
    
    while True:
        try:
            porcentaje = int(input("Porcentaje de descuento: ").strip())
            break
        except ValueError:
            print("Debe ser un numero entero\n")

    for i in range(len(inventario)):
        inventario[i]["precio"] -= (porcentaje*inventario[i]["precio"])/100

def total(inventario):
    """Muestra el precio total del inventario"""
    if not inventario:
        print("No hay productos registrados.")
        return
    
    total_inventario = 0
    for i in range(len(inventario)):
        total_inventario += (inventario[i]["cantidad"] * inventario[i]["precio"])

    print("Precio total del inventario: " + str(total_inventario))


# --------- Programa principal --------- #

inventario = []

while True:
    menu()
    opcion = input("Selecciona una opción: ").strip()

    if opcion == "1":
        nombre = input("Nombre: ").strip().lower()
        while True:
            try:
                precio = float(input("Precio: ").strip())
                break
            except ValueError:
                print("Debe ser un numero\n")
        
        while True:
            try:
                cantidad = int(input("Cantidad: ").strip())
                break
            except ValueError:
                print("Debe ser un numero entero\n")

        producto = crear_producto(nombre,precio,cantidad)
        inventario.append(producto)

        print("Producto " + nombre + " añadido correctamente.")

    elif opcion == "2":
        mostrar_lista(inventario)

    elif opcion == "3":
        vender_producto(inventario)

    elif opcion == "4":
        descuento(inventario)

    elif opcion == "5":
        total(inventario)

    elif opcion == "6":
        print("Saliendo...")
        break

    else:
        print("Opcion no disponible")