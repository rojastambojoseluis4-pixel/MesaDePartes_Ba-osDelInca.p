import os

MAX_EXPEDIENTES = 100
FILE_PATH = "expedientes_banos.txt"

# ARREGLOS PARALELOS
codigos = [""] * MAX_EXPEDIENTES
ciudadanos = [""] * MAX_EXPEDIENTES
asuntos = [""] * MAX_EXPEDIENTES
fechas = [""] * MAX_EXPEDIENTES
cantidad = 0

def registrar_expediente():
    """Opción 1: Registrar expediente con validaciones según el algoritmo"""
    global cantidad
    os.system("cls" if os.name == "nt" else "clear")
    if cantidad < 100:
        codigo = input("Ingrese el codigo del expediente: ").strip()
        encontrado = False
        for i in range(cantidad):
            if codigos[i] == codigo:
                encontrado = True
                break
        if encontrado:
            print("Error: el codigo ya existe.")
        else:
            ciudadano = input("Ingrese el nombre del ciudadano: ").strip()
            asunto = input("Ingrese el asunto: ").strip()
            fecha = input("Ingrese la fecha de recepcion: ").strip()
            if ciudadano != "" and asunto != "" and fecha != "":
                codigos[cantidad] = codigo
                ciudadanos[cantidad] = ciudadano
                asuntos[cantidad] = asunto
                fechas[cantidad] = fecha
                cantidad += 1
                print("Expediente registrado correctamente.")
            else:
                print("Error: los campos no pueden estar vacios.")
    else:
        print("Error: se alcanzo el limite de expedientes.")
    input("\nPresione Enter para continuar...")

def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(":::SISTEMA DE MESA DE PARTES:::")
        print("1. Registrar expediente")
        print("2. Buscar expediente")
        print("3. Ordenar expedientes")
        print("4. Mostrar expedientes")
        print("0. Salir")
        opcion = input("Ingrese una opcion: ").strip()
        if opcion == "1": registrar_expediente()
        elif opcion == "0": break
if __name__ == "__main__":
    main()
