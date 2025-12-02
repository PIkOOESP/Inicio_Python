import os
import csv

# Esta direccion se debe cambiar si el programa no funciona
os.chdir(os.getcwd()+ "/Practica_06/Ejercicio3")

# ---------- Funciones ----------

ARCHIVO = "contactos.csv"
CAMPOS = ["nombre", "telefono", "email", "ciudad"]

with open(ARCHIVO, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=CAMPOS)
    writer.writeheader()

def menu():
    print("\n========= AGENDA DE CONTACTOS =========")
    print("1. Añadir contacto")
    print("2. Listar contactos")
    print("3. Buscar contactos por ciudad")
    print("4. Exportar contactos de una ciudad a CSV")
    print("5. Importar contactos desde un CSV externo")
    print("6. Salir")


def añadir_contacto():
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    ciudad = input("Ciudad: ")

    with open(ARCHIVO, "a", newline="", encoding="utf-8") as fichero:
        writer = csv.DictWriter(fichero, fieldnames=CAMPOS)
        writer.writerow({
            "nombre": nombre,
            "telefono": telefono,
            "email": email,
            "ciudad": ciudad
        })

    print("Contacto añadido correctamente.")

def listar_contactos():
    with open(ARCHIVO, "r", encoding="utf-8") as fichero:
        reader = csv.DictReader(fichero)
        for row in reader:
            print(row['nombre'] + "-" + str(row['telefono']) + "-" + row['email'] + "-" + row['ciudad'])

def buscar_por_ciudad():
    ciudad = input("\nIntroduce la ciudad a buscar: ").strip().lower()

    with open(ARCHIVO, "r", encoding="utf-8") as fichero:
        reader = csv.DictReader(fichero)
        encontrados = False

        for row in reader:
            if row["ciudad"].lower() == ciudad:
                print(row['nombre'] + "-" + str(row['telefono']) + "-" + row['email'])
                encontrados = True

        if encontrados == False:
            print("No hay contactos en esa ciudad.")

def exportar_por_ciudad():
    ciudad = input("\nCiudad a exportar: ").strip().lower()
    archivo_salida = "contactos_" + ciudad + ".csv"

    with open(ARCHIVO, "r", encoding="utf-8") as fichero_ex, \
         open(archivo_salida, "w", newline="", encoding="utf-8") as fichero_in:

        reader = csv.DictReader(fichero_ex)
        writer = csv.DictWriter(fichero_in, fieldnames=CAMPOS)
        writer.writeheader()

        n_exportados = 0
        for row in reader:
            if row["ciudad"].lower() == ciudad:
                writer.writerow(row)
                num_exportados += 1

    print("Exportados " + str(n_exportados) + " contactos a " + archivo_salida)


def importar_csv():
    ruta = input("\nIntroduce la ruta del CSV a importar: ")

    if not os.path.exists(ruta):
        print("El archivo no existe.")
        return

    with open(ruta, "r", encoding="utf-8") as fichero_ex, \
         open(ARCHIVO, "a", newline="", encoding="utf-8") as fichero_in:

        reader = csv.DictReader(fichero_ex)
        writer = csv.DictWriter(fichero_in, fieldnames=CAMPOS)

        n_importados = 0
        for row in reader:
            if all(campo in row for campo in CAMPOS):
                writer.writerow(row)
                importados += 1

    print("Importados " + str(n_importados) + " contactos desde " + ruta)

# ---------- Programa principal ----------
while True:
    menu()

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        añadir_contacto()
    elif opcion == "2":
        listar_contactos()
    elif opcion == "3":
        buscar_por_ciudad()
    elif opcion == "4":
        exportar_por_ciudad()
    elif opcion == "5":
        importar_csv()
    elif opcion == "6":
        print("Saliendo...")
        break
    else: 
        print("Opcion no valida")