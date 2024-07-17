import sqlite3

def crear_tablas():
    conexion_bd = sqlite3.connect('base_de_datos.db')
    cursor = conexion_bd.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pacientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        edad INTEGER,
        genero TEXT,
        correo TEXT,
        telefono TEXT,
        contrasena TEXT,
        alergias TEXT,
        enfermedades TEXT,
        medicamentos_actuales TEXT,
        antecedentes_familiares TEXT,
        habitos TEXT,
        numero_atencion INTEGER
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS medicos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        especialidad TEXT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS administradores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS asignaciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        paciente_id INTEGER,
        medico_id INTEGER,
        FOREIGN KEY(paciente_id) REFERENCES pacientes(id),
        FOREIGN KEY(medico_id) REFERENCES medicos(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS diagnosticos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        paciente_id INTEGER,
        diagnostico TEXT,
        FOREIGN KEY(paciente_id) REFERENCES pacientes(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS recetas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        paciente_id INTEGER,
        medicamento TEXT,
        FOREIGN KEY(paciente_id) REFERENCES pacientes(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS examenes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        paciente_id INTEGER,
        examen TEXT,
        FOREIGN KEY(paciente_id) REFERENCES pacientes(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS citas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        paciente_id INTEGER,
        hora TEXT,
        FOREIGN KEY(paciente_id) REFERENCES pacientes(id)
    )
    ''')

    conexion_bd.commit()
    conexion_bd.close()

if __name__ == '__main__':
    crear_tablas()
    print("Tablas creadas exitosamente en la base de datos.")
