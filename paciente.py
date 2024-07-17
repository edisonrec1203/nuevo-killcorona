import conexion
import random

def registrar_paciente():
    conexion_bd = conexion.conectar()
    cursor = conexion_bd.cursor()

    nombre = input("Ingrese el nombre: ")
    edad = input("Ingrese la edad: ")
    genero = input("Ingrese el género: ")
    correo = input("Ingrese el correo: ")
    telefono = input("Ingrese el teléfono: ")
    contrasena = input("Ingrese la contraseña: ")
    alergias = input("Ingrese las alergias: ")
    enfermedades = input("Ingrese las enfermedades: ")
    medicamentos_actuales = input("Ingrese los medicamentos actuales: ")
    antecedentes_familiares = input("Ingrese los antecedentes familiares: ")
    habitos = input("Ingrese los hábitos: ")
    username = input("Ingrese el nombre de usuario: ")

    cursor.execute('''
        INSERT INTO pacientes (
            nombre, edad, genero, correo, telefono, contrasena, alergias, 
            enfermedades, medicamentos_actuales, antecedentes_familiares, habitos
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (nombre, edad, genero, correo, telefono, contrasena, alergias, 
          enfermedades, medicamentos_actuales, antecedentes_familiares, habitos))

    cursor.execute('''
        INSERT INTO users (username, password, role)
        VALUES (?, ?, 'paciente')
    ''', (username, contrasena))

    conexion_bd.commit()
    conexion_bd.close()
    print("Paciente registrado exitosamente!")

def asignar_numero_atencion():
    conexion_bd = conexion.conectar()
    cursor = conexion_bd.cursor()

    paciente_id = input("Ingrese el ID del paciente: ")

    # Obtener todos los números de atención actuales
    cursor.execute('SELECT numero_atencion FROM pacientes WHERE numero_atencion IS NOT NULL')
    numeros_ocupados = [row[0] for row in cursor.fetchall()]

    # Encontrar un número disponible del 1 al 100 aleatoriamente
    numeros_disponibles = list(set(range(1, 101)) - set(numeros_ocupados))
    if numeros_disponibles:
        nuevo_numero = random.choice(numeros_disponibles)
    else:
        print("No hay números de atención disponibles.")
        conexion_bd.close()
        return

    # Asignar el número de atención al paciente
    cursor.execute('''
        UPDATE pacientes
        SET numero_atencion = ?
        WHERE id = ?
    ''', (nuevo_numero, paciente_id))

    conexion_bd.commit()
    conexion_bd.close()
    print(f"Número de atención asignado: {nuevo_numero}")

def seleccionar_medico_general():
    conexion_bd = conexion.conectar()
    cursor = conexion_bd.cursor()

    paciente_id = input("Ingrese el ID del paciente: ")

    cursor.execute('''
        SELECT id, nombre FROM medicos WHERE especialidad = 'General'
    ''')

    medicos = cursor.fetchall()
    if medicos:
        print("Médicos Generales Disponibles:")
        for medico in medicos:
            print(f"ID: {medico[0]}, Nombre: {medico[1]}")
        
        medico_id = int(input("Ingrese el ID del médico general que desea seleccionar: "))
        cursor.execute('''
            INSERT INTO asignaciones (paciente_id, medico_id)
            VALUES (?, ?)
        ''', (paciente_id, medico_id))

        conexion_bd.commit()
        print("Médico general asignado exitosamente.")
        
        # Simular consulta y derivación a especialista si es necesario
        derivar = input("¿Desea derivar al paciente a un especialista? (si/no): ")
        if derivar.lower() == 'si':
            cursor.execute('''
                SELECT id, nombre, especialidad FROM medicos WHERE especialidad != 'General'
            ''')
            especialistas = cursor.fetchall()
            if especialistas:
                print("Especialistas Disponibles:")
                for especialista in especialistas:
                    print(f"ID: {especialista[0]}, Nombre: {especialista[1]}, Especialidad: {especialista[2]}")
                
                especialista_id = int(input("Ingrese el ID del especialista que desea seleccionar: "))
                cursor.execute('''
                    UPDATE asignaciones
                    SET medico_id = ?
                    WHERE paciente_id = ?
                ''', (especialista_id, paciente_id))

                conexion_bd.commit()
                print("Paciente derivado a especialista exitosamente.")
            else:
                print("No hay especialistas disponibles.")
    else:
        print("No hay médicos generales disponibles.")

    conexion_bd.close()

def ver_numero_atencion():
    conexion_bd = conexion.conectar()
    cursor = conexion_bd.cursor()

    paciente_id = input("Ingrese el ID del paciente: ")

    cursor.execute('''
        SELECT numero_atencion FROM pacientes WHERE id = ?
    ''', (paciente_id,))
    
    numero_atencion = cursor.fetchone()
    if numero_atencion:
        print(f"Número de atención asignado: {numero_atencion[0]}")
    else:
        print("No se encontró un número de atención asignado para este paciente.")
    
    conexion_bd.close()

def ver_medico_asignado():
    conexion_bd = conexion.conectar()
    cursor = conexion_bd.cursor()

    paciente_id = input("Ingrese el ID del paciente: ")
    cursor.execute('''
        SELECT medico_id FROM asignaciones WHERE paciente_id = ?
    ''', (paciente_id,))
    
    medico_id = cursor.fetchone()
    if medico_id:
        cursor.execute('''
            SELECT nombre FROM medicos WHERE id = ?
        ''', (medico_id[0],))
        medico = cursor.fetchone()
        if medico:
            print(f"El médico asignado es: {medico[0]}")
        else:
            print("No se encontró el médico asignado.")
    else:
        print("No se encontró una asignación para el paciente.")
    
    conexion_bd.close()

def ver_hora_atencion():
    conexion_bd = conexion.conectar()
    cursor = conexion_bd.cursor()

    paciente_id = input("Ingrese el ID del paciente: ")
    cursor.execute('''
        SELECT hora FROM citas WHERE paciente_id = ?
    ''', (paciente_id,))
    
    cita = cursor.fetchone()
    if cita:
        print(f"La hora de atención es: {cita[0]}")
    else:
        print("No se encontró una cita para el paciente.")
    
    conexion_bd.close()
