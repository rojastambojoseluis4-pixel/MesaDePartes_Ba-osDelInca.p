import os

MAX_EXPEDIENTES = 100
codigos = [""] * MAX_EXPEDIENTES
ciudadanos = [""] * MAX_EXPEDIENTES
asuntos = [""] * MAX_EXPEDIENTES
total_expedientes = 0

def buscar_indice_por_codigo(codigo_buscar):
    for i in range(total_expedientes):
        if codigos[i].lower() == codigo_buscar.lower(): return i
    return -1

def registrar_expediente():
    global total_expedientes
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- REGISTRO DE NUEVO EXPEDIENTE EDIL ---")
    while True:
        codigo = input("Ingrese código del expediente: ").strip().upper()
        if not codigo: continue
        if buscar_indice_por_codigo(codigo) != -1: continue
        break
    ciudadano = input("Ingrese nombre completo: ").strip().upper()
    asunto = input("Ingrese el asunto: ").strip().upper()
    codigos[total_expedientes] = codigo
    ciudadanos[total_expedientes] = ciudadano
    asuntos[total_expedientes] = asunto
    total_expedientes += 1
