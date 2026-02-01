# ==================================================
# PROYECTO INTEGRADOR - SISTEMA DE GESTIÓN DE JUGADORES
# ==================================================
#
# OBJETIVO GENERAL:
# Crear un sistema que permita gestionar jugadores de un juego,
# guardarlos en un archivo y recuperarlos, aplicando TODOS los
# conceptos vistos hasta ahora.
#
# --------------------------------------------------
# TEMAS QUE DEBE INTEGRAR OBLIGATORIAMENTE:
# - Variables
# - Operadores
# - Condicionales
# - Bucles
# - Colecciones (listas y diccionarios)
# - Funciones
# - Excepciones (try / except / else)
# - Programación Orientada a Objetos (POO)
# - Métodos de strings (strip, split, lower, upper, isdigit, etc.)
# - Módulos (crear al menos un módulo propio)
# - Archivos (with as, read, write, append)
# --------------------------------------------------
#
# ==================================================
# PARTE 1 - CLASE JUGADOR (POO)
# ==================================================
#
# Crear una clase llamada Jugador
#
# La clase debe tener:
# - Atributos:
#   * nombre (str)
#   * nivel (int)
#   * vida (int)
#   * inventario (lista de strings)
#
# - Métodos:
#   * __init__
#   * mostrar_info() -> imprime todos los datos del jugador
#   * subir_nivel() -> aumenta el nivel en 1
#   * recibir_daño(cantidad) -> reduce la vida sin que baje de 0
#
# Validaciones:
# - nombre no puede estar vacío
# - nivel y vida deben ser enteros positivos
#
# Manejar errores con excepciones donde corresponda
#
# ==================================================
# PARTE 2 - FUNCIONES DE UTILIDAD (FUNCIONES + STRINGS)
# ==================================================
#
# Crear funciones que:
#
# 1) Soliciten datos al usuario:
#    - Nombre del jugador
#    - Nivel
#    - Vida
#    - Inventario separado por comas
#
# 2) Limpien los datos ingresados:
#    - strip()
#    - lower() o capitalize() para nombres
#    - split(",") para inventario
#
# 3) Validen:
#    - Que nivel y vida sean numéricos
#    - Que el inventario tenga al menos un item
#
# Si hay errores:
# - Mostrar mensajes claros
# - Evitar que el programa se rompa
#
# ==================================================
# PARTE 3 - COLECCIONES Y BUCLES
# ==================================================
#
# Crear una lista que almacene objetos Jugador
#
# Implementar un menú que se repita hasta que el usuario elija salir:
#
# 1 - Crear nuevo jugador
# 2 - Mostrar todos los jugadores
# 3 - Subir nivel a un jugador
# 4 - Guardar jugadores en archivo
# 5 - Cargar jugadores desde archivo
# 6 - Salir
#
# Usar bucles y condicionales para controlar el flujo
#
# ==================================================
# PARTE 4 - ARCHIVOS
# ==================================================
#
# Guardar los jugadores en un archivo de texto:
#
# - Nombre del archivo: jugadores.txt
# - Cada jugador en una línea
# - Formato sugerido:
#   nombre;nivel;vida;item1,item2,item3
#
# Requisitos:
# - Usar with open(...)
# - encoding="utf-8"
# - Manejar FileNotFoundError y OSError
#
# ==================================================
# PARTE 5 - CARGA DESDE ARCHIVO
# ==================================================
#
# Leer el archivo jugadores.txt
#
# - Parsear cada línea usando split(";") y split(",")
# - Crear objetos Jugador a partir de los datos
# - Agregarlos a la lista de jugadores
#
# Validar:
# - Que el archivo exista
# - Que los datos tengan el formato correcto
#
# ==================================================
# PARTE 6 - MÓDULOS
# ==================================================
#
# Separar el proyecto en al menos DOS archivos:
#
# - jugador.py -> clase Jugador
# - main.py -> lógica principal del programa
#
# Importar correctamente la clase Jugador
#
# ==================================================
# PARTE 7 - EXCEPCIONES
# ==================================================
#
# Usar try / except / else en:
# - Conversión de tipos
# - Lectura y escritura de archivos
# - Acceso a índices de listas
#
# No permitir que el programa se corte inesperadamente
#
# ==================================================
# FIN DEL PROYECTO
# ==================================================

# ----------------------MODULOS--------------------------- #
import jugadores as j

# ---------------------FUNCIONES-------------------------- #
def guardar_jugadores_en_archivo(jugadores):
    jugadores_formateados = []
    for jugador in jugadores:
        jugadores_formateados.append(j.formatear_jugador(jugador))
    try:
        with open("code/Ejercicio-Integrador-Jugadores/jugadores.txt", "a", encoding="utf-8") as file:
            for jugador_formateado in jugadores_formateados:
                file.write(jugador_formateado + "\n")
    except OSError as e:
        print(f"Error al intentar abrir el archivo:", e)
    else:
        print(f"Se guardo a los jugadores: {jugadores_formateados}")
        print("Manipulación de escritura del archivo completada correctamente!")


def leer_jugadores_de_archivo():
    jugadores = []
    jugadores_formateados = []
    try:
        with open("code/Ejercicio-Integrador-Jugadores/jugadores.txt", "r", encoding="utf-8") as file:
            jugadores_formateados = file.readlines()
    except FileNotFoundError:
        print("No se encontró el archivo")
    except OSError as e:
        print(f"Error al intentar abrir el archivo:", e)
    else:
        print("Lectura del archivo completada correctamente!")
        for jugador_formateado in jugadores_formateados:
            jugadores.append(j.desformatear_jugador(jugador_formateado))
    finally:
        return jugadores

# --------------------- VARIABLES -------------------------- # 
opciones_menu = {   1:"Crear nuevo jugador",
                    2:"Mostrar todos los jugadores",
                    3:"Subir nivel a un jugador",
                    4:"Guardar jugadores en archivo",
                    5:"Cargar jugadores desde archivo",
                    6:"salir"}

lista_de_jugadores = []
opcion_seleccionada = True

# ------------------------ MENÚ----------------------------- #
print("Bienvenido al menú!")
while opcion_seleccionada:
    
    print("-----------OPCIONES------------")
    for key,value in opciones_menu.items():
        print(f"# {key} - {value}")
    """ 
    print("# 1 - Crear nuevo jugador")
    print("# 2 - Mostrar todos los jugadores")
    print("# 3 - Subir nivel a un jugador")
    print("# 4 - Guardar jugadores en archivo")
    print("# 5 - Cargar jugadores desde archivo")
    print("# 6 - Salir") 
    """

    # INPUT
    try:
        opcion_seleccionada = int(input("Ingresa el número correspondiente a acción a realizar: "))
    except ValueError:
        print("El valor ingresado no es numérico, vuelva a intentarlo con un valor válido")
        continue
    else:
        print(f"Opción seleccionada: {opcion_seleccionada} - {opciones_menu.get(opcion_seleccionada, "No Disponible")}")

    # ACCION
    match opcion_seleccionada:
        # 1 - Crear nuevo jugador
        case 1:
            nuevo_jugador = j.crear_jugador()
            lista_de_jugadores.append(nuevo_jugador)
            print("Se agregó al nuevo jugador a la lista! volviendo al menú...")
        # 2 - Mostrar todos los jugadores
        case 2:
            for jugador in lista_de_jugadores:
                print(f"Mostrando jugador Nro {lista_de_jugadores.index(jugador) + 1}: ")
                jugador.mostrar_info()
        # 3 - Subir nivel a un jugador
        case 3:
            nombre = input("Ingrese el nombre del jugador que desea subir de nivel: ")
            jugadorEncontrado = False
            for jugador in lista_de_jugadores:
                if jugador.nombre == nombre:
                    jugador.subir_nivel()
                    jugadorEncontrado = True
                    break
            if jugadorEncontrado:
                print("Level Up completado correctamente! :D")
            else:
                print("Jugador no encontrado :C")
        # 4 - Guardar jugadores en archivo
        case 4:
            if len(lista_de_jugadores):
                guardar_jugadores_en_archivo(lista_de_jugadores)
            else:
                print("No hay jugadores para guardar en el archivo")
        # 5 - Cargar jugadores desde archivo
        case 5:
            jugadores_archivados = leer_jugadores_de_archivo()
            if len(jugadores_archivados):
                for jugador_archivado in jugadores_archivados:
                    lista_de_jugadores.append(jugador_archivado)
                    print(f"Se carga el jugador: {jugador_archivado.nombre}")
            else:
                print("No hay jugadores archivados para cargar")
        # 6 - salir
        case 6:
            print("Finalizando Menú, Adiós! :D")
            break
        # DEFAULT - reintentar input
        case _:
            print("Acción no reconocida, vuelva a intentarlo ingresando un valor válido")
            continue


