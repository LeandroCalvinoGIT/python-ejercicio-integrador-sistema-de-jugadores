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

import random
nombres_por_defecto = ["Steve", "Juan", "Mary", "Alex"]

class Jugador():
    def __init__(self, nombre, nivel, vida, inventario):
        # nombre no puede estar vacío
        if nombre != "":
            self.nombre = nombre
        else:
            print("El nombre del jugador no puede estar vacío, asignando nombre por defecto")
            self.nombre = random.choice(nombres_por_defecto)
        # nivel y vida deben ser enteros positivos
        if nivel > 0:
            self.nivel = nivel
        else:
            print("El nivel del jugador no puede ser negativo o 0, asignando nivel por defecto (1)")
            self.nivel = 1
        if vida >= 0:
            self.vida = vida
        else:
            print("La vida del jugador no puede ser negativa, asignando nivel por defecto (100)")
            self.vida = 100
        self.inventario = inventario
    
    # Imprime todos los datos del jugador
    def mostrar_info(self):
        print("-----Resumen de Jugador-----")
        print(f"Nombre: {self.nombre}")
        print(f"Nivel: {self.nivel}")
        print(f"Puntos de vida: {self.vida}")
        print(f"Inventario: {self.inventario}")
        print("----------------------------")
    
    # Aumenta el nivel en 1
    def subir_nivel(self):
        self.nivel+=1
        print(f"El nivel de {self.nombre} ha aumentado! Nivel actual: {self.nivel}")

    # Reduce la vida sin que baje de 0
    def recibir_danio(self,cantidad):
        if self.vida == 0:
            print(f"El jugador {self.nombre} ya está muerto, no puede seguir recibiendo daño")
        if self.vida - cantidad <= 0:
            self.vida = 0
            print(f"El jugador {self.nombre} no resiste ese ataque, y muere")
        else:
            self.vida -= cantidad
            print(f"El jugador {self.nombre} recibió {cantidad} puntos de daño, vida restante: {self.vida}")

# FUNCIONES

# Nombre
def solicitar_nombre():
    nombre = input("Ingrese el nombre del jugador: ").strip().lower().capitalize()
    return nombre

# Nivel y Vida
def validar_valor_numerico(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        print("Error: El valor ingresado no es númerico")
        return "error"

def solicitar_numero():
    numero = input("ingrese un numero: ").strip()
    numero = validar_valor_numerico(numero)
    if numero != "error":
        return numero
    else:
        return solicitar_numero()
        
def solicitar_nivel():
    print("Nivel del jugador ->")
    nivel = solicitar_numero()
    return nivel

def solicitar_vida():
    print("Cantidad de puntos de vida del jugador ->")
    vida = solicitar_numero()
    return vida

# Inventario
def solicitar_inventario():
    entrada = input("Ingrese los items del inventario en formato \"item1, item2\": ")
    items = entrada.split(",")
    inventario = []

    for indice, item in enumerate(items):
        # Limpio item
        item = item.strip().lower().capitalize()
        # Si el item está vacío no lo agrego al inventario
        if item == "" or item == " " or item == "\n":
            print(f"El item ingresado nro {indice + 1} está vacío, por lo que no se ingresa al inventario")
            continue
        # Si no está vacío, lo agrego ya formateado
        inventario.append(item)

    if len(inventario):
        return inventario
    else:
        print("El inventario debe tener al menos un item")
        return solicitar_inventario()
    
def crear_jugador():
    nombre = solicitar_nombre()
    nivel = solicitar_nivel()
    vida = solicitar_vida()
    inventario = solicitar_inventario()

    jugador = Jugador(nombre, nivel, vida, inventario)

    print("Se creó al jugador correctamente!")

    jugador.mostrar_info()

    return jugador

def formatear_jugador(jugador):
    # FORMATO:  nombre;nivel;vida;item1,item2,item3
    jugador_formateado = jugador.nombre + ";" + str(jugador.nivel) + ";" + str(jugador.vida) + ";" + ",".join(jugador.inventario)
    # print(jugador_formateado)
    return jugador_formateado

def desformatear_jugador(jugador_formateado):
    atributos = jugador_formateado.split(";")
    nombre = atributos[0]
    nivel = int(atributos[1])
    vida = int(atributos[2])
    inventario = atributos[3].split(",")
    jugador = Jugador(nombre,nivel, vida, inventario)
    return jugador

# MAIN DE PRUEBA 
if __name__ == "__main__":

    jugador_modelo = Jugador("nombre",1, 100,["Uno,Dos,Tres"])
    jugador_modelo.mostrar_info()
    jugador2 = desformatear_jugador(formatear_jugador(jugador_modelo))
    jugador2.subir_nivel()
    jugador2.mostrar_info()
