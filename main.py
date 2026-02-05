""""
Programa principal - Punto de entrada
"""
from database import crear_tabla
from interfaz import mostrar_menu, listar_contactos, agregar_contacto, buscar_contacto

def main():
    """Funcion principal del programa"""
    #1. Preparar la base de datos
    crear_tabla()

    #2. Bucle principal del menú
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opcion(1-4): ").strip()

        if opcion == "1":
            listar_contactos()
        elif opcion == "2":
            agregar_contacto()
        elif opcion == "3":
            buscar_contacto()
        elif opcion == "4":
            print("\n🖐️ ¡Hasta luego!")
            break
        else:
            print("❌ Opcion incorrecta. Elige 1, 2, 3 o 4")

    # Punto de entrada del programa
if __name__ == "__main__":
    main()
