from database import obtener_conexion

def agregar(nombre, telefono, email):
    """Agrega un nuevo contacto"""
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(
        "INSERT INTO contactos (nombre, telefono, email) VALUES (?, ?, ?)",
        (nombre, telefono, email)
    )

    conexion.commit()
    conexion.close()
    print(f"✅ Contacto '{nombre}' agregado")
    

def listar_todos():
    """Lista todos los contactos"""
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM contactos")
    contactos = cursor.fetchall()
        

    conexion.close()
    return contactos
    
       
def buscar_por_nombre(nombre):
    """Busca contactos que contengan el nombre"""
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT * FROM contactos WHERE nombre LIKE ?",
            (f'%{nombre}%',)
    )
    resultados = cursor.fetchall()

    conexion.close()
    return resultados




    