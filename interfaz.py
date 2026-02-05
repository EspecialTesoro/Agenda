""""
Interfaz de usuario simple
"""
from operaciones import agregar, listar_todos, buscar_por_nombre
    
def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*40)
    print("       AGENDA DE CONTACTOS")
    print("="*40)
    print("1. Listar contactos")
    print("2. Agregar contacto")
    print("3. Buscar contacto")
    print("4. Salir")
    print("="*40)


def listar_contactos():
    """Muestra todos los contactos"""
    contactos = listar_todos()

    if not contactos:
        print("👎 No hay contactos")
        return

    print("\n🟨 LISTA DE CONTACTOS:")
    for id_contacto, nombre, telefono, email in contactos:
        print(f"    {id_contacto}, {nombre}")
        if telefono:
            print(f"      📞 {telefono}")
        if email:
            print(f"      📧 {email}")
        print()
   

def agregar_contacto():
    """Pide datos para nuevo contacto"""
    print("\n + NUEVO CONTACTO")
    nombre = input("Nombre: ").strip()
    telefono = input("Teléfono (opcional): ").strip() 
    email = input("Email (opcional): ").strip() 

    if nombre: #Solo agregar si tiene nombre
        agregar(nombre, telefono or None, email or None)
    else:
        print("❌ El nombre es obligatorio")
       

def buscar_contacto():
    """Busca un contacto por nombre"""
    print("\n 🔍BUSCAR CONTACTO")
    nombre = input("Buscar: ").strip()

    if not nombre:
        print("⚠️Escribe algo para buscar")
        return

    resultados = buscar_por_nombre(nombre)

    if resultados:
        print(f"\n🔍 Encontrados {len(resultados)} contactos:")
        for id_contacto, nombre, telefono, email in resultados:
            print(f"   {nombre}")
            if telefono:
                print(f"      Tel: {telefono}")
                   
    else:
        print(f" ❌  No se encontró '{nombre}'")
