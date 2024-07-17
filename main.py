from rich.console import Console
from rich.prompt import Prompt
import paciente
import medico
import administrador
import conexion  # Importa el módulo de conexión a la base de datos

console = Console()

def menu_principal():
    while True:
        console.print("[bold cyan]Menú Principal[/bold cyan]", justify="center")
        console.print("1. Registrarse", justify="center")
        console.print("2. Iniciar Sesión", justify="center")
        console.print("3. Salir", justify="center")

        opcion = Prompt.ask("Seleccione una opción", choices=["1", "2", "3"])

        if opcion == "1":
            menu_registro()
        elif opcion == "2":
            menu_login()
        elif opcion == "3":
            break

def menu_registro():
    console.print("[bold cyan]Registro[/bold cyan]", justify="center")
    console.print("1. Registrarse como Médico", justify="center")
    console.print("2. Registrarse como Administrador", justify="center")
    console.print("3. Registrarse como Paciente", justify="center")
    console.print("4. Volver", justify="center")

    opcion = Prompt.ask("Seleccione una opción", choices=["1", "2", "3", "4"])

    if opcion == "1":
        medico.registrar_medico()
    elif opcion == "2":
        administrador.registrar_administrador()
    elif opcion == "3":
        paciente.registrar_paciente()
    elif opcion == "4":
        menu_principal()

def menu_login():
    console.print("[bold cyan]Inicio de Sesión[/bold cyan]", justify="center")
    username = Prompt.ask("Usuario")
    password = Prompt.ask("Contraseña", password=True)

    # Autenticar usuario (asumiendo que existe una función 'authenticate_user' en 'conexion.py')
    user_data = conexion.authenticate_user(username, password)

    if user_data:
        role = user_data["role"]
        if role == "medico":
            menu_medico()
        elif role == "administrador":
            menu_administrador()
        elif role == "paciente":
            menu_paciente()
    else:
        console.print("[bold red]Credenciales incorrectas[/bold red]", justify="center")
        menu_login()

def menu_medico():
    while True:
        console.print("[bold cyan]Menú Médico[/bold cyan]", justify="center")
        console.print("1. Ver lista de pacientes", justify="center")
        console.print("2. Recetar medicamentos", justify="center")
        console.print("3. Realizar exámenes", justify="center")
        console.print("4. Agregar diagnóstico", justify="center")
        console.print("5. Atender pacientes", justify="center")
        console.print("6. Volver", justify="center")

        opcion = Prompt.ask("Seleccione una opción", choices=["1", "2", "3", "4", "5", "6"])

        if opcion == "1":
            medico.ver_pacientes()
        elif opcion == "2":
            medico.recetar_medicamentos()
        elif opcion == "3":
            medico.realizar_examenes()
        elif opcion == "4":
            medico.agregar_diagnostico()
        elif opcion == "5":
            medico.atender_paciente()
        elif opcion == "6":
            break

def menu_administrador():
    while True:
        console.print("[bold cyan]Menú Administrador[/bold cyan]", justify="center")
        console.print("1. Editar datos", justify="center")
        console.print("2. Eliminar usuarios", justify="center")
        console.print("3. Volver", justify="center")

        opcion = Prompt.ask("Seleccione una opción", choices=["1", "2", "3"])

        if opcion == "1":
            administrador.editar_datos()
        elif opcion == "2":
            administrador.eliminar_usuarios()
        elif opcion == "3":
            break

def menu_paciente():
    while True:
        console.print("[bold cyan]Menú Paciente[/bold cyan]", justify="center")
        console.print("1. Seleccionar médico general", justify="center")
        console.print("2. Ver número de atención", justify="center")
        console.print("3. Asignar número de atención", justify="center")
        console.print("4. Volver", justify="center")

        opcion = Prompt.ask("Seleccione una opción", choices=["1", "2", "3", "4"])

        if opcion == "1":
            paciente.seleccionar_medico_general()
        elif opcion == "2":
            paciente.ver_numero_atencion()
        elif opcion == "3":
            paciente.asignar_numero_atencion()
        elif opcion == "4":
            break

if __name__ == "__main__":
    menu_principal()
