import os

MAX_EXPEDIENTES = 100

# ARREGLOS PARALELOS (Listas coordinadas por índice)
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
                ciudadanos[cantidad] = ciudadano
                asuntos[cantidad] = asunto
                fechas[cantidad] = fecha
                codigos[cantidad] = codigo
                cantidad += 1
                print("Expediente registrado correctamente.")
            else:
                print("Error: los campos no pueden estar vacios.")
    else:
        print("Error: se alcanzo el limite de expedientes.")
        
    input("\nPresione Enter para continuar...")
