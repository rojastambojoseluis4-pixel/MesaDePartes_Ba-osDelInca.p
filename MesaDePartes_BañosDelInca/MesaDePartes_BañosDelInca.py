import os

MAX_EXPEDIENTES = 100
FILE_PATH = "expedientes_banos.txt"

codigos = [""] * MAX_EXPEDIENTES
ciudadanos = [""] * MAX_EXPEDIENTES
asuntos = [""] * MAX_EXPEDIENTES
fechas = [""] * MAX_EXPEDIENTES
cantidad = 0

def registrar_expediente():
    global cantidad
    os.system("cls" if os.name == "nt" else "clear")
    if cantidad < 100:
        codigo = input("Ingrese el codigo del expediente: ").strip()
        encontrado = False
        for i in range(cantidad):
            if codigos[i] == codigo: encontrado = True; break
        if encontrado:
            print("Error: el codigo ya existe.")
        else:
            ciudadano = input("Ingrese el nombre del ciudadano: ").strip()
            asunto = input("Ingrese el asunto: ").strip()
            fecha = input("Ingrese la fecha de recepcion: ").strip()
            if ciudadano != "" and asunto != "" and fecha != "":
                codigos[cantidad] = codigo; ciudadanos[cantidad] = ciudadano; asuntos[cantidad] = asunto; fechas[cantidad] = fecha; cantidad += 1
                print("Expediente registrado correctamente.")
            else: print("Error: los campos no pueden estar vacios.")
    input("\nPresione Enter para continuar...")

def buscar_expediente():
    os.system("cls" if os.name == "nt" else "clear")
    codigo = input("Ingrese el codigo que desea buscar: ").strip()
    encontrado = False
    for i in range(cantidad):
        if codigos[i] == codigo:
            print("Expediente encontrado:\nCodigo: ", codigos[i], "\nCiudadano: ", ciudadanos[i], "\nAsunto: ", asuntos[i], "\nFecha: ", fechas[i])
            encontrado = True
    if not encontrado: print("No se encontro el expediente.")
    input("\nPresione Enter para continuar...")

def ordenar_expedientes():
    os.system("cls" if os.name == "nt" else "clear")
    if cantidad > 1:
        for i in range(cantidad - 1):
            for j in range(i + 1, cantidad):
                if codigos[i] > codigos[j]:
                    codigos[i], codigos[j] = codigos[j], codigos[i]
                    ciudadanos[i], ciudadanos[j] = ciudadanos[j], ciudadanos[i]
                    asuntos[i], asuntos[j] = asuntos[j], asuntos[i]
                    fechas[i], fechas[j] = fechas[j], fechas[i]
        print("Expedientes ordenados por codigo.")
    else: print("No hay suficientes expedientes para ordenar.")
    input("\nPresione Enter para continuar...")

def mostrar_expedientes():
    os.system("cls" if os.name == "nt" else "clear")
    if cantidad == 0: print("No hay expedientes registrados.")
    else:
        for i in range(cantidad):
            print("--------------------------\nCodigo: ", codigos[i], "\nCiudadano: ", ciudadanos[i], "\nAsunto: ", asuntos[i], "\nFecha: ", fechas[i])
    input("\nPresione Enter para continuar...")

def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(":::SISTEMA DE MESA DE PARTES:::\n1. Registrar expediente\n2. Buscar expediente\n3. Ordenar expedientes\n4. Mostrar expedientes\n0. Salir")
        opcion = input("Ingrese una opcion: ").strip()
        if opcion == "1": registrar_expediente()
        elif opcion == "2": buscar_expediente()
        elif opcion == "3": ordenar_expedientes()
        elif opcion == "4": mostrar_expedientes()
        elif opcion == "0": break
if __name__ == "__main__": main()
