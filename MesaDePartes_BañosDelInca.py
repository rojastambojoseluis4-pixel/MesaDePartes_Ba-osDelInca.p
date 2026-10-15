import os

MAX_EXPEDIENTES = 100
FILE_PATH = "expedientes_banos.txt"

codigos = [""] * MAX_EXPEDIENTES
ciudadanos = [""] * MAX_EXPEDIENTES
asuntos = [""] * MAX_EXPEDIENTES
total_expedientes = 0

def cargar_datos_desde_archivo():
    global total_expedientes
    if not os.path.exists(FILE_PATH): return
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            total_expedientes = 0
            for linea in f:
                linea = linea.strip()
                if not linea or total_expedientes >= MAX_EXPEDIENTES: continue
                campos = linea.split("|")
                if len(campos) == 3:
                    codigos[total_expedientes] = campos[0]
                    ciudadanos[total_expedientes] = campos[1]
                    asuntos[total_expedientes] = campos[2]
                    total_expedientes += 1
    except Exception as e: print(f"Error al cargar archivo: {e}")

def guardar_datos_en_archivo():
    try:
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            for i in range(total_expedientes):
                f.write(f"{codigos[i]}|{ciudadanos[i]}|{asuntos[i]}\n")
    except Exception as e: print(f"Error al guardar archivo: {e}")

def buscar_indice_por_codigo(codigo_buscar):
    for i in range(total_expedientes):
        if codigos[i].lower() == codigo_buscar.lower(): return i
    return -1

def registrar_expediente():
    global total_expedientes
    os.system("cls" if os.name == "nt" else "clear")
    print("--- REGISTRO DE NUEVO EXPEDIENTE EDIL ---")
    if total_expedientes >= MAX_EXPEDIENTES: return
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
    guardar_datos_en_archivo()

def buscar_expediente():
    os.system("cls" if os.name == "nt" else "clear")
    codigo_buscar = input("Ingrese el código exacto a buscar: ").strip()
    idx = buscar_indice_por_codigo(codigo_buscar)
    if idx != -1:
        print(f"\n📌 EXPEDIENTE ENCONTRADO:\nCódigo: {codigos[idx]}\nCiudadano: {ciudadanos[idx]}\nAsunto: {asuntos[idx]}")
    else: print("\n❌ Alerta: No se encontró ningún expediente.")
    input("\nPresione Enter...")

def ordenar_y_mostrar_expedientes():
    os.system("cls" if os.name == "nt" else "clear")
    if total_expedientes == 0: return
    c_cod, c_ciu, c_asu = codigos[:total_expedientes], ciudadanos[:total_expedientes], asuntos[:total_expedientes]
    for i in range(total_expedientes - 1):
        for j in range(total_expedientes - i - 1):
            if c_cod[j] > c_cod[j + 1]:
                c_cod[j], c_cod[j + 1] = c_cod[j + 1], c_cod[j]
                c_ciu[j], c_ciu[j + 1] = c_ciu[j + 1], c_ciu[j]
                c_asu[j], c_asu[j + 1] = c_asu[j + 1], c_asu[j]
    for i in range(total_expedientes):
        print(f"[{c_cod[i]}] Ciudadano: {c_ciu[i]} | Asunto: {c_asu[i]}")
    input("\nPresione Enter...")

def main():
    cargar_datos_desde_archivo()
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(" 1. Registrar nuevo expediente\n 2. Buscar expediente\n 3. Ordenar y mostrar\n 4. Salir")
        opcion = input("Seleccione una opción (1-4): ").strip()
        if opcion == "1": registrar_expediente()
        elif opcion == "2": buscar_expediente()
        elif opcion == "3": ordenar_y_mostrar_expedientes()
        elif opcion == "4": break

if __name__ == "__main__":
    main()
