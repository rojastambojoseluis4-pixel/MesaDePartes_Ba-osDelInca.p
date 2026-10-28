import os

MAX_EXPEDIENTES = 100
FILE_PATH = "expedientes_banos.txt"

codigos = [None] * MAX_EXPEDIENTES
ciudadanos = [None] * MAX_EXPEDIENTES
asuntos = [None] * MAX_EXPEDIENTES
fechas = [None] * MAX_EXPEDIENTES
cantidad = 0


def cargar_datos_desde_archivo():
    """Módulo de Persistencia: Carga automática de datos al iniciar el programa"""
    global cantidad
    if not os.path.exists(FILE_PATH):
        return
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            cantidad = 0
            for linea in f:
                linea = linea.strip()
                if not linea or cantidad >= MAX_EXPEDIENTES:
                    continue
                campos = linea.split("|")
                if len(campos) == 4:
                    codigos[cantidad] = campos[0]
                    ciudadanos[cantidad] = campos[1]
                    asuntos[cantidad] = campos[2]
                    fechas[cantidad] = campos[3]
                    cantidad += 1
    except Exception as e:
        print(f"Error al cargar archivo: {e}")


def guardar_datos_en_archivo():
    """Módulo de Persistencia: Escritura física en disco plano"""
    try:
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            for i in range(cantidad):
                f.write(f"{codigos[i]}|{ciudadanos[i]}|{asuntos[i]}|{fechas[i]}\n")
    except Exception as e:
        print(f"Error al guardar archivo: {e}")


def registrar_expediente():
    """Opción 1: Registrar expediente con validaciones según el algoritmo"""
    global cantidad  # <-- ESTA LÍNEA SOLUCIONA EL ERROR
    
    os.system("cls" if os.name == "nt" else "clear")
    if cantidad < MAX_EXPEDIENTES:
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
                guardar_datos_en_archivo()
                print("Expediente registrado correctamente.")
            else:
                print("Error: los campos no pueden estar vacios.")
    else:
        print("Error: se alcanzo el limite de expedientes.")
    input("\nPresione Enter para continuar...")


def buscar_expediente():
    """Opción 2: Buscar expediente por código"""
    os.system("cls" if os.name == "nt" else "clear")
    codigo = input("Ingrese el codigo que desea buscar: ").strip()
    encontrado = False
    for i in range(cantidad):
        if codigos[i] == codigo:
            print("Expediente encontrado:")
            print("Codigo:", codigos[i])
            print("Ciudadano:", ciudadanos[i])
            print("Asunto:", asuntos[i])
            print("Fecha:", fechas[i])
            encontrado = True
            break
    if not encontrado:
      print("No se encontro el expediente.")
    input("\nPresione Enter para continuar...")


def ordenar_expedientes():
    """Opción 3: Ordenar arreglos en paralelo usando método Burbuja síncrono"""
    os.system("cls" if os.name == "nt" else "clear")
    if cantidad > 1:
        for i in range(cantidad - 1):
            for j in range(i + 1, cantidad):
                if codigos[i] > codigos[j]:
                    codigos[i], codigos[j] = codigos[j], codigos[i]
                    ciudadanos[i], ciudadanos[j] = ciudadanos[j], ciudadanos[i]
                    asuntos[i], asuntos[j] = asuntos[j], asuntos[i]
                    fechas[i], fechas[j] = fechas[j], fechas[i]
        guardar_datos_en_archivo()
        print("Expedientes ordenados por codigo.")
    else:
        print("No hay suficientes expedientes para ordenar.")
    input("\nPresione Enter para continuar...")


def mostrar_expedientes():
    """Opción 4: Recorrer y mostrar los expedientes registrados"""
    os.system("cls" if os.name == "nt" else "clear")
    if cantidad == 0:
        print("No hay expedientes registrados.")
    else:
        for i in range(cantidad):
            print("--------------------------")
            print("Codigo:", codigos[i])
            print("Ciudadano:", ciudadanos[i])
            print("Asunto:", asuntos[i])
            print("Fecha:", fechas[i])
    input("\nPresione Enter para continuar...")


def main():
    """Menú Principal Interactivo"""
    cargar_datos_desde_archivo()
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(":::SISTEMA DE MESA DE PARTES:::")
        print("1. Registrar expediente")
        print("2. Buscar expediente")
        print("3. Ordenar expedientes")
        print("4. Mostrar expedientes")
        print("0. Salir")
        opcion = input("Ingrese una opcion: ").strip()
        if opcion == "1":
            registrar_expediente()
        elif opcion == "2":
            buscar_expediente()
        elif opcion == "3":
            ordenar_expedientes()
        elif opcion == "4":
            mostrar_expedientes()
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion no valida. Intente nuevamente.")
        input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    main()