import os

# CONSTANTES Y CONFIGURACIÓN
MAX_EXPEDIENTES = 100
FILE_PATH = "expedientes_banos.txt"

# ARREGLOS PARALELOS (Listas coordinadas por índice)
codigos = [""] * MAX_EXPEDIENTES
ciudadanos = [""] * MAX_EXPEDIENTES
asuntos = [""] * MAX_EXPEDIENTES
fechas = [""] * MAX_EXPEDIENTES
cantidad = 0

def cargar_datos_desde_archivo():
    """Carga automática de datos al iniciar el programa"""
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
                # Separación de los 4 campos usando el delimitador '|'
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
    """Escritura física de los datos guardados en el archivo de texto"""
    try:
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            for i in range(cantidad):
                f.write(f"{codigos[i]}|{ciudadanos[i]}|{asuntos[i]}|{fechas[i]}\n")
    except Exception as e:
        print(f"Error al guardar archivo: {e}")

def registrar_expediente():
    """Opción 1: Registrar expediente con validaciones según el algoritmo"""
    global cantidad
    os.system("cls" if os.name == "nt" else "clear")
    
    if cantidad < 100:
        codigo = input("Ingrese el codigo del expediente: ").strip()
        
        # Validar si el código ya existe
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
            
            # Validación de campos vacíos
            if ciudadano != "" and asunto != "" and fecha != "":
                ciudadanos[cantidad] = ciudadano
                asuntos[cantidad] = asunto
                fechas[cantidad] = fecha
                codigos[cantidad] = codigo
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
            print(f"Codigo: {codigos[i]}")
            print(f"Ciudadano: {ciudadanos[i]}")
            print(f"Asunto: {asuntos[i]}")
            print(f"Fecha: {fechas[i]}")
            encontrado = True
            break # Detiene la búsqueda al encontrarlo
            
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
                    # Intercambio síncrono de todos los arreglos paralelos
                    codigos[i], codigos[j] = codigos[j], codigos[i]
                    ciudadanos[i], ciudadanos[j] = ciudadanos[j], ciudadanos[i]
                    asuntos[i], asuntos[j] = asuntos[j], asuntos[i]
                    fechas[i], fechas[j] = fechas[j], fechas[i]
        guardar_datos_en_archivo() # Guarda el nuevo orden en el archivo
        print("Expedientes ordenados por codigo.")
    else:
        print("No hay suficientes expedientes para ordenar.")
        
    input("\nPresione Enter para continuar...")

def mostrar_expedientes():
    """Opción 4: Listar todos los expedientes registrados"""
    os.system("cls" if os.name == "nt" else "clear")
    if cantidad == 0:
        print("No hay expedientes registrados.")
    else:
        for i in range(cantidad):
            print("--------------------------")
            print(f"Codigo: {codigos[i]}")
            print(f"Ciudadano: {ciudadanos[i]}")
            print(f"Asunto: {asuntos[i]}")
            print(f"Fecha: {fechas[i]}")
            
    input("\nPresione Enter para continuar...")

def main():
    """Menú Principal interactivo (Repetir - Hasta Que)"""
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
