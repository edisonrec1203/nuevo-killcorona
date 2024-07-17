import conexion
import sqlite3

def registrar_administrador():
    conexion_bd = conexion.conectar()
    cursor = conexion_bd.cursor()

    nombre = input("Ingrese el nombre: ")
    username = input("Ingrese el nombre de usuario: ")
    password = input("Ingrese la contraseña: ")

    try:
        cursor.execute('''
            INSERT INTO administradores (nombre, username, password)
            VALUES (?, ?, ?)
        ''', (nombre, username, password))

        cursor.execute('''
            INSERT INTO users (username, password, role)
            VALUES (?, ?, 'administrador')
        ''', (username, password))

        conexion_bd.commit()
        print("Administrador registrado exitosamente!")
    except sqlite3.IntegrityError:
        print("Error: El nombre de usuario ya existe. Por favor, elija otro nombre de usuario.")
    finally:
        conexion_bd.close()

def editar_datos():
    conexion_bd = conexion.conectar()
    cursor = conexion_bd.cursor()

    tipo_usuario = input("Ingrese el tipo de usuario a editar (paciente/medico): ").strip().lower()
    
    if tipo_usuario == 'paciente':
        paciente_id = input("Ingrese el ID del paciente a editar: ")
        print("Opciones de edición:")
        print("1. Nombre")
        print("2. Edad")
        print("3. Género")
        print("4. Correo")
        print("5. Teléfono")
        print("6. Contraseña")
        print("7. Alergias")
        print("8. Enfermedades")
        print("9. Medicamentos actuales")
        print("10. Antecedentes familiares")
        print("11. Hábitos")
        
        opcion = input("Seleccione el campo a editar (1-11): ")

        nuevo_valor = input("Ingrese el nuevo valor: ")
        campo = ""

        if opcion == "1":
            campo = "nombre"
        elif opcion == "2":
            campo = "edad"
        elif opcion == "3":
            campo = "genero"
        elif opcion == "4":
            campo = "correo"
        elif opcion == "5":
            campo = "telefono"
        elif opcion == "6":
            campo = "contrasena"
        elif opcion == "7":
            campo = "alergias"
        elif opcion == "8":
            campo = "enfermedades"
        elif opcion == "9":
            campo = "medicamentos_actuales"
        elif opcion == "10":
            campo = "antecedentes_familiares"
        elif opcion == "11":
            campo = "habitos"

        cursor.execute(f'''
            UPDATE pacientes
            SET {campo} = ?
            WHERE id = ?
        ''', (nuevo_valor, paciente_id))

    elif tipo_usuario == 'medico':
        medico_id = input("Ingrese el ID del médico a editar: ")
        print("Opciones de edición:")
        print("1. Nombre")
        print("2. Especialidad")
        print("3. Nombre de usuario")
        print("4. Contraseña")

        opcion = input("Seleccione el campo a editar (1-4): ")

        nuevo_valor = input("Ingrese el nuevo valor: ")
        campo = ""

        if opcion == "1":
            campo = "nombre"
        elif opcion == "2":
            campo = "especialidad"
        elif opcion == "3":
            campo = "username"
        elif opcion == "4":
            campo = "password"

        cursor.execute(f'''
            UPDATE medicos
            SET {campo} = ?
            WHERE id = ?
        ''', (nuevo_valor, medico_id))

    conexion_bd.commit()
    conexion_bd.close()
    print("Datos actualizados exitosamente!")

def eliminar_usuarios():
    conexion_bd = conexion.conectar()
    cursor = conexion_bd.cursor()

    tipo_usuario = input("Ingrese el tipo de usuario a eliminar (paciente/medico/administrador): ").strip().lower()
    
    usuario_id = input(f"Ingrese el ID del {tipo_usuario} a eliminar: ")

    if tipo_usuario == "paciente":
        cursor.execute('DELETE FROM pacientes WHERE id = ?', (usuario_id,))
    elif tipo_usuario == "medico":
        cursor.execute('DELETE FROM medicos WHERE id = ?', (usuario_id,))
    elif tipo_usuario == "administrador":
        cursor.execute('DELETE FROM administradores WHERE id = ?', (usuario_id,))

    cursor.execute('DELETE FROM users WHERE id = ?', (usuario_id,))

    conexion_bd.commit()
    conexion_bd.close()
    print(f"{tipo_usuario.capitalize()} eliminado exitosamente!")
