import os

def main():
    """Función de Control de Flujo Principal"""
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("====================================================")
        print("     MUNICIPALIDAD DISTRITAL DE BAÑOS DEL INCA      ")
        print("          SISTEMA DE MESA DE PARTES DIGITAL         ")
        print("====================================================")
        print(" 1. Registrar nuevo expediente")
        print(" 2. Buscar expediente por código")
        print(" 3. Ordenar y mostrar expedientes")
        print(" 4. Salir de la aplicación")
        print("====================================================")
        
        opcion = input("Seleccione una opción (1-4): ").strip()
        if opcion == "4":
            print("\nCerrando el sistema... ¡Hasta luego!")
            break
