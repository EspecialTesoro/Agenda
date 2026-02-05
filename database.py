"""
Manejo simple de la base de datos
"""


import sqlite3


def crear_tabla():
    """Crea la tabla de contactos si no existe"""
    conexion = sqlite3.connect('agenda.db')
    cursor = conexion.cursor()

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS contactos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                telefono TEXT,
                email TEXT
            )
        ''')

    conexion.commit()
    conexion.close()
    print("✅ Base de datos lista")


def obtener_conexion():
    """Devuelve una conexión a la base de datos"""
    return sqlite3.connect('agenda.db')





       