import os
MAX_EXPEDIENTES = 100
codigos = [""] * MAX_EXPEDIENTES
ciudadanos = [""] * MAX_EXPEDIENTES
asuntos = [""] * MAX_EXPEDIENTES
fechas = [""] * MAX_EXPEDIENTES
cantidad = 0

def buscar_expediente():
    """Opción 2: Buscar expediente por código"""
    os.system("cls" if os.name == "nt" else "clear")
    codigo = input("Ingrese el codigo que desea buscar: ").strip()
    encontrado = False
    for i in range(cantidad):
        if codigos[i] == codigo:
            print("Expediente encontrado:")
            encontrado = True
            break
    if not encontrado:
        print("No se encontro el expediente.")
    input("\nPresione Enter para continuar...")

def ordenar_expedientes():
    """Opción 3: Ordenar arreglos en paralelo usando método Burbuja"""
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
    input("\nPresione Enter para continuar...")
