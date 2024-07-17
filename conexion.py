import sqlite3

def conectar():
    return sqlite3.connect('base_de_datos.db')

def authenticate_user(username, password):
    conexion_bd = conectar()
    cursor = conexion_bd.cursor()
    
    cursor.execute('''
        SELECT id, role FROM users WHERE username = ? AND password = ?
    ''', (username, password))
    
    user = cursor.fetchone()
    conexion_bd.close()
    
    if user:
        return {"id": user[0], "role": user[1]}
    else:
        return None
