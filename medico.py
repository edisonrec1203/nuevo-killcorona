import conexion

def registrar_medico():
    conexion_bd = conexion.conectar()
    cursor = conexion_bd.cursor()

    nombre = input("Ingrese el nombre: ")
    especialidad = input("Ingrese la especialidad: ")
    username = input("Ingrese el nombre de usuario: ")
    password = input("Ingrese la contraseña: ")

    cursor.execute('''
        INSERT INTO medicos (nombre, especialidad, username, password)
        VALUES (?, ?, ?, ?)
    ''', (nombre, especialidad, username, password))

    cursor.execute('''
        INSERT INTO users (username, password, role)
        VALUES (?, ?, 'medico')
    ''', (username, password))

    conexion_bd.commit()
    conexion_bd.close()
    print("Médico registrado exitosamente!")

def ver_pacientes():
    conexion_bd = conexion.conectar()
    cursor = conexion_bd.cursor()

    cursor.execute('''
        SELECT id, nombre, edad, genero, correo, telefono, numero_atencion
        FROM pacientes
        WHERE numero_atencion IS NOT NULL
        ORDER BY numero_atencion
    ''')

    pacientes = cursor.fetchall()
    if pacientes:
        print("Lista de Pacientes con Número de Atención:")
        for paciente in pacientes:
            print(f"ID: {paciente[0]}, Nombre: {paciente[1]}, Edad: {paciente[2]}, Género: {paciente[3]}, Correo: {paciente[4]}, Teléfono: {paciente[5]}, Número de Atención: {paciente[6]}")
    else:
        print("No hay pacientes con números de atención asignados.")

    conexion_bd.close()

def atender_paciente():
    conexion_bd = conexion.conectar()
    cursor = conexion_bd.cursor()

    # Mostrar la lista de pacientes en espera
    cursor.execute('''
        SELECT id, nombre, numero_atencion
        FROM pacientes
        WHERE numero_atencion IS NOT NULL
    ''')

    pacientes = cursor.fetchall()
    if pacientes:
        print("Lista de Pacientes en Espera:")
        for paciente in pacientes:
            print(f"ID: {paciente[0]}, Nombre: {paciente[1]}, Número de Atención: {paciente[2]}")
    else:
        print("No hay pacientes en espera.")
        conexion_bd.close()
        return

    paciente_id = int(input("Ingrese el ID del paciente a atender: "))

    cursor.execute('''
        SELECT id, nombre, edad, genero, correo, telefono
        FROM pacientes
        WHERE id = ?
    ''', (paciente_id,))

    paciente = cursor.fetchone()
    if paciente:
        print(f"Atendiendo al paciente con ID {paciente_id}:")
        print(f"ID: {paciente[0]}, Nombre: {paciente[1]}, Edad: {paciente[2]}, Género: {paciente[3]}, Correo: {paciente[4]}, Teléfono: {paciente[5]}")
        
        # Aquí puedes agregar la lógica para atender al paciente (por ejemplo, agregar un diagnóstico, prescribir medicamentos, etc.)
        diagnostico = input("Ingrese el diagnóstico: ")
        cursor.execute('''
            INSERT INTO diagnosticos (paciente_id, diagnostico)
            VALUES (?, ?)
        ''', (paciente[0], diagnostico))

        # Remover el número de atención después de la atención
        cursor.execute('''
            UPDATE pacientes
            SET numero_atencion = NULL
            WHERE id = ?
        ''', (paciente[0],))

        conexion_bd.commit()
        print("Paciente atendido y número de atención removido.")
    else:
        print("No se encontró un paciente con ese ID.")

    conexion_bd.close()

def recetar_medicamentos():
    conexion_bd = conexion.conectar()
    cursor = conexion_bd.cursor()

    paciente_id = input("Ingrese el ID del paciente: ")
    medicamento = input("Ingrese el medicamento: ")

    cursor.execute('''
        INSERT INTO recetas (paciente_id, medicamento)
        VALUES (?, ?)
    ''', (paciente_id, medicamento))

    conexion_bd.commit()
    conexion_bd.close()
    print("Medicamento recetado exitosamente!")

def realizar_examenes():
    conexion_bd = conexion.conectar()
    cursor = conexion_bd.cursor()

    paciente_id = input("Ingrese el ID del paciente: ")
    examen = input("Ingrese el examen: ")

    cursor.execute('''
        INSERT INTO examenes (paciente_id, examen)
        VALUES (?, ?)
    ''', (paciente_id, examen))

    conexion_bd.commit()
    conexion_bd.close()
    print("Examen registrado exitosamente!")

def agregar_diagnostico():
    conexion_bd = conexion.conectar()
    cursor = conexion_bd.cursor()

    paciente_id = input("Ingrese el ID del paciente: ")
    diagnostico = input("Ingrese el diagnóstico: ")

    cursor.execute('''
        INSERT INTO diagnosticos (paciente_id, diagnostico)
        VALUES (?, ?)
    ''', (paciente_id, diagnostico))

    conexion_bd.commit()
    conexion_bd.close()
    print("Diagnóstico agregado exitosamente!")
