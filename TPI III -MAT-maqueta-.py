
import random

def mostrar_compuertas(nombre,a,b, z):
    print(f"{a}  {nombre}  {b}  →  {z}")
    
def imprimir_matriz(matriz, encabezado=None):
    if encabezado:
        print(*[v.center(6) for v in encabezado])
    for fila in matriz:
        print(*[str(elem).center(6) for elem in fila])
        
def generar_combinaciones(n):
    """Genera todas las combinaciones binarias para n variables."""
    combinaciones = []
    total = 2 ** n
    for i in range(total):
        binario = bin(i)[2:]    # Convertimos a binario sin el '0b'
        cantidad_ceros = n - len(binario)   # Cuántos ceros faltan
        binario = "0" * cantidad_ceros + binario
        fila = [int(c) for c in binario]    # Convierte cada caráctera entero
        combinaciones.append(fila) 
    return combinaciones

def operacion_and(fila):    
    for elemento in fila:
        if elemento == 0:
            return 0
    return 1

def operacion_or(fila):
    for elemento in fila:
        if elemento == 1:
            return 1
    return 0

def operacion_not(fila):
    for elemento in fila:
        if elemento == 1:
            return 0
    return 1
def puerta_and(a, b):
    return a & b

def puerta_or(a, b):
    return a | b

def puerta_not(a):
    return 1 - a

def puerta_nand(a, b):
    return 1 - (a & b)

def puerta_nor(a, b):
    return 1 - (a | b)

def puerta_xor(a, b):
    return int(a != b)

def pedir_bit(texto):
    while True:
        try:
            valor = int(input(texto))
            if valor in (0,1):
                return valor
            else:
                print("❌ Solo se permite ingresar 0 o 1.\n")
        except ValueError:
            print("❌ Dato incorrecto, solo se acepta 0 y 1")

def mostrar_bool_selec():
    print(f"Expresión: {expresion}\n")


def menu_continuar(tipo):
    """Pregunta si continuar con la misma operación o volver al menú principal."""
    print("\n¿Qué deseas hacer ahora?")
    print(f"1️⃣ - {tipo}\n2️⃣ - Volver al menú principal\n")
    try:
        opcion = int(input("👉🏽 Elija una opción: "))
        return opcion == 1
    except ValueError:
        print("❌ Entrada inválida. Volviendo al menú principal.\n")
        return False


# ---- Funciones del juego de adivinanza ----

def jugar_adivinanza(numero_decimal, es_binario_a_decimal=False):
    """
    Función general para jugar a adivinar conversiones binario-decimal.
    - si es_binario_a_decimal=False: muestra decimal, adivina binario
    - si es_binario_a_decimal=True: muestra binario, adivina decimal
    """
    binario = bin(numero_decimal)[2:]
    intentos = 5
    
    while intentos > 0:
        if es_binario_a_decimal:
            print(f"Número en binario: {binario}")
            respuesta = input(f"Intento {6 - intentos}/5 - Ingresa el decimal: ").strip()
            try:
                respuesta_valor = int(respuesta)
            except ValueError:
                print("❌ Debes ingresar un número entero.\n")
                continue
        else:
            print(f"Número decimal: {numero_decimal}")
            respuesta = input(f"Intento {6 - intentos}/5 - Ingresa el binario: ").strip()
            if not respuesta or any(c not in '01' for c in respuesta):
                print("❌ Debes ingresar solo 0s y 1s.\n")
                continue
            respuesta_valor = int(respuesta, 2)
        
        if respuesta_valor == numero_decimal:
            if es_binario_a_decimal:
                print(f"✅ ¡Adivinaste! {binario} en decimal es: {numero_decimal}\n")
            else:
                print(f"✅ ¡Adivinaste! {numero_decimal} en binario es: {binario}\n")
            return
        
        intentos -= 1
        if intentos > 0:
            pista = "mayor" if respuesta_valor < numero_decimal else "menor"
            print(f"❌ El número es {pista}. Intentos restantes: {intentos}\n")
        else:
            if es_binario_a_decimal:
                print(f"❌ Se agotaron los intentos. La respuesta era: {numero_decimal}\n")
            else:
                print(f"❌ Se agotaron los intentos. La respuesta era: {binario}\n")


def juego_decimal_a_binario():
    """Mostrar un número decimal y pedir adivinar su binario."""
    numero_decimal = random.randint(1, 100)
    jugar_adivinanza(numero_decimal, es_binario_a_decimal=False)    # False → se muestra DECIMAL y el usuario debe escribir el BINARIO


def juego_binario_a_decimal():
    """Mostrar un número en binario y pedir adivinar su decimal."""
    numero_decimal = random.randint(1, 100)
    jugar_adivinanza(numero_decimal, es_binario_a_decimal=True)      # True → se muestra BINARIO y el usuario debe escribir el DECIMAL


def menu_juego_binario():
    """Menú para elegir el tipo de juego."""
    salir_juego = False
    
    while not salir_juego:  # Bucle del menú del juego; se repite hasta que el usuario elija salir
        print(
            "\n--- MENÚ JUEGO BINARIO ---\n"
            "1️⃣ - Decimal → Binario\n"
            "2️⃣ - Binario → Decimal\n"
            "3️⃣ - Volver al menú principal\n"
        )
        
        try:
            opcion = int(input("👉🏽 Elija una opción: "))
        except ValueError:
            print("❌ Entrada inválida. Intenta de nuevo.\n")
            continue
        
        if opcion == 1:
            juego_decimal_a_binario()
            input("Presiona ENTER para volver al menú de juegos...")
        elif opcion == 2:
            juego_binario_a_decimal()
            input("Presiona ENTER para volver al menú de juegos...")
        elif opcion == 3:
            salir_juego = True
        else:
            print("❌ Opción inválida. Intenta de nuevo.\n")

# ---- Fin funciones del juego ----

mostrar_menuPrincipal = True

while mostrar_menuPrincipal:
    print(
        "\n========== MENÚ PRINCIPAL ==========\n"
        "0️⃣ - Salir\n"
        "1️⃣ - Simulador de Puertas Lógicas\n"
        "2️⃣ - Tablas de Verdad\n"
        "3️⃣ - Juego Binario\n"
    )
    
    try:
        eleccion = int(input("👉🏽 Elección: "))
        
        match eleccion:
            case 0:
                mostrar_menuPrincipal = False
                print("\n🚫 Programa Finalizado 🚫")
            case 1:
                # Diccionario con puertas lógicas: nombre y función
                puertas = {
                    1: ("AND", puerta_and),
                    2: ("OR", puerta_or),
                    3: ("NOT", puerta_not),
                    4: ("NAND", puerta_nand),
                    5: ("NOR", puerta_nor),
                    6: ("XOR", puerta_xor)
                }
                
                salir_puertas = False
                while not salir_puertas:
                    print(
                        "\n=== SIMULADOR DE PUERTAS LÓGICAS ===\n"
                        "1️⃣ - AND\n" 
                        "2️⃣ - OR\n" 
                        "3️⃣ - NOT\n"
                        "4️⃣ - NAND\n"
                        "5️⃣ - NOR\n"
                        "6️⃣ - XOR\n"
                        )
                    try:
                        op = int(input("👉🏽 Seleccione una opción del menú: "))
                        if op not in puertas:
                            print("❌ Opción inválida.\n")
                            continue
                        
                        a = pedir_bit("👉🏽 Ingrese el valor A (0 o 1): ")
                        b = pedir_bit("👉🏽 Ingrese el valor B (0 o 1): ")
                        
                        nombre, funcion = puertas[op]
                        
                        # Calcular resultado según si es NOT o no
                        if op == 3:
                            z = funcion(a)
                            print(f"{nombre} {a}  →  {z}\n")
                        else:
                            z = funcion(a, b)
                            mostrar_compuertas(nombre, a, b, z)
                            print()
                        
                        # Menú de continuación
                        salir_puertas = not menu_continuar("Elegir otra puerta lógica")
                    except ValueError:
                        print("❌ Entrada inválida.\n")
                        continue
            case 2:
                salir_tablas = False
                while not salir_tablas:
                    print("\n===== MENÚ DE OPERACIONES BOOLEANAS =====\n")
                    print(
                        "1️⃣ - AND\n"
                        "2️⃣ - OR\n"
                        "3️⃣ - NOT\n"
                    )
                    opcion = int(input("👉🏽 Elija una opción: "))
                    while opcion < 1 or opcion > 3:
                        print("Opción inválida. Por favor intete de nuevo 🤗")
                        opcion = int(input("👉🏽 Elija una opción: "))
                        
                    cantidad_v = int(input("👉🏽 Ingrese la cantidad de variables: "))
                    variables = [chr(65 + i) for i in range(cantidad_v)]   # A, B, C...
                    comb = generar_combinaciones(cantidad_v)
                    print("\nVariables detectadas:", variables)
                    
                    match opcion:
                        case 1:
                            expresion = " AND ".join(variables)
                            mostrar_bool_selec()
                        case 2:
                            expresion = " OR ".join(variables)
                            mostrar_bool_selec()
                        case 3:
                            expresion = "NOT (" + " OR ".join(variables) + ")"
                            mostrar_bool_selec()
                    
                    encabezado = variables + ["Z"]
                    matriz = []
                    for fila in comb:
                        match opcion:
                            case 1:        # AND
                                z = operacion_and(fila)
                                matriz.append(fila + [z])
                            case 2:      # OR
                                z = operacion_or(fila)
                                matriz.append(fila + [z])
                            case 3:                  # NOT aplicado al conjunto completo
                                z = operacion_not(fila)
                                matriz.append(fila + [z])
                    
                    imprimir_matriz(matriz, encabezado)
                    
                    # Menú después de mostrar la tabla
                    print("\n¿Qué deseas hacer ahora?")
                    print(
                        "1️⃣ - Generar otra tabla de verdad\n"
                        "2️⃣ - Volver al menú principal\n"
                    )
                    
                    try:
                        continuar = int(input("👉🏽 Elija una opción: "))
                        if continuar == 1:
                            salir_tablas = False
                        elif continuar == 2:
                            salir_tablas = True
                        else:
                            print("❌ Opción inválida. Volviendo al menú principal.\n")
                            salir_tablas = True
                    except ValueError:
                        print("❌ Entrada inválida. Volviendo al menú principal.\n")
                        salir_tablas = True
            case 3:
                # Llamar al menú del juego
                menu_juego_binario()
            case _:
                print("Opción no válida.")
    except ValueError:
        print("🚫 La entrada ingresada no es válida. 🚫")