import os

def main():
    """Menú Principal interactivo (Repetir - Hasta Que)"""
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(":::SISTEMA DE MESA DE PARTES:::")
        print("1. Registrar expediente")
        print("2. Buscar expediente")
        print("3. Ordenar expedientes")
        print("4. Mostrar expedientes")
        print("0. Salir")
        
        opcion = input("Ingrese una opcion: ").strip()
        
        if opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion no valida. Intente nuevamente.")
            input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()
