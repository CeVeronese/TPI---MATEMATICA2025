def ingresar_dnis():                           # Pide al usuario cuántos DNIs quiere ingresar.
    dnis = []
    n = int(input("¿Cuántos DNIs quiere ingresar?: "))
    i = 0
    while i < n:
        dni = input("Ingrese DNI " + str(i+1) + ": ")
        dnis.append(dni)
        i += 1
    return dnis

def digitos_unicos(dni):                       # Recorre cada dígito y guarda solo los que no se repiten en una nueva lista "unicos".
    unicos = []
    i = 0
    while i < len(dni):
        d = dni[i]
        j = 0
        encontrado = False
        while j < len(unicos):
            if unicos[j] == d:
                encontrado = True
            j += 1
        if not encontrado:
            unicos.append(d)
        i += 1
    return unicos

 # Operaciones de conjuntos

def union(d1, d2):                             # Devuelve todos los elementos de ambos, sin repetir.                       
    resultado = []
    i = 0
    while i < len(d1):
        if d1[i] not in resultado:
            resultado.append(d1[i])
        i += 1

    j = 0
    while j < len(d2):
        if d2[j] not in resultado:
            resultado.append(d2[j])
        j += 1

    return resultado

def interseccion(d1, d2):                    # Devuelve los elementos que aparecen en los dos.
    resultado = []
    i = 0
    while i < len(d1):
        d = d1[i]
        j = 0
        while j < len(d2):
            if d == d2[j] and d not in resultado:
                resultado.append(d)
            j += 1
        i += 1
    return resultado

def diferencia(d1, d2):                      # Devuelve los que están en d1 pero no en d2.
    resultado = []
    i = 0
    while i < len(d1):
        d = d1[i]
        j = 0
        encontrado = False
        while j < len(d2):
            if d == d2[j]:
                encontrado = True
            j += 1
        if not encontrado:
            resultado.append(d)
        i += 1
    return resultado

def diferencia_simetrica(d1, d2):           # Devuelve los que están en uno u otro, pero no en ambos.
    dif1 = diferencia(d1, d2)
    dif2 = diferencia(d2, d1)

    resultado = []
    i = 0
    while i < len(dif1):
        resultado.append(dif1[i])
        i += 1
    j = 0
    while j < len(dif2):
        resultado.append(dif2[j])
        j += 1
    return resultado

def contar_frecuencias(dni):                # Cuenta cuántas veces aparece cada número en el DNI.
    print("\nDNI:", dni)
    digitos = "0123456789"
    i = 0
    while i < len(digitos):
        d = digitos[i]
        contador = 0
        j = 0
        while j < len(dni):
            if dni[j] == d:
                contador += 1
            j += 1
        if contador > 0:
            print("Dígito", d, ":", contador, "vez/veces")
        i += 1

def suma_digitos(dni):                     # Convierte cada dígito en número entero y suma todos los dígitos.

    suma = 0
    i = 0
    while i < len(dni):
        suma += int(dni[i])
        i += 1
    return suma

# Se ingresan los DNIs.

dnis = ingresar_dnis()                   # Se calculan sus dígitos únicos.
lista_unicos = []
i = 0
while i < len(dnis):
    unicos = digitos_unicos(dnis[i])
    lista_unicos.append(unicos)                       

    if len(unicos) > 6:
        print("DNI", i+1, "-> Diversidad numérica alta")  # Si tiene más de 6 dígitos diferentes, muestra "Diversidad numérica alta".

    i += 1

print("\n--- Operaciones entre pares ---")   # Operaciones (unión, intersección, diferencia, etc.) entre cada par de DNIs.
i = 0
while i < len(lista_unicos):
    j = i + 1
    while j < len(lista_unicos):
        d1 = lista_unicos[i]
        d2 = lista_unicos[j]
        print("\nDNI" + str(i+1) + " y DNI" + str(j+1) + ":")
        print("Unión:", union(d1, d2))
        print("Intersección:", interseccion(d1, d2))
        print("Diferencia (DNI" + str(i+1) + " - DNI" + str(j+1) + "):", diferencia(d1, d2))
        print("Diferencia Simétrica:", diferencia_simetrica(d1, d2))
        j += 1
    i += 1

print("\n--- Frecuencias y Sumas ---")   # Muestra las frecuencias de cada dígito y la suma de dígitos para cada DNI.
i = 0
while i < len(dnis):
    contar_frecuencias(dnis[i])
    print("Suma de dígitos:", suma_digitos(dnis[i]))
    i += 1

print("\n--- Condiciones Globales ---")   # Busca si algún dígito aparece en todos los DNIs y lo muestra.
digitos = "0123456789"
i = 0
while i < len(digitos):
    d = digitos[i]
    aparece_en_todos = True
    j = 0
    while j < len(lista_unicos):
        if d not in lista_unicos[j]:
            aparece_en_todos = False
        j += 1
    if aparece_en_todos:
        print("Dígito compartido:", d)
    i += 1

# Trabajo con años y edades

def ingresar_anios():       # Pide cuántos integrantes hay, se ingresan sus años de nacimiento y se guardan en una lista.
    anios = []
    n = int(input("¿Cuántos integrantes?: "))
    i = 0
    while i < n:
        anio = int(input("Ingrese año de nacimiento del integrante " + str(i+1) + ": "))
        anios.append(anio)
        i += 1
    return anios

def es_bisiesto(anio):               # Devuelve True si el año es bisiesto.
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

def contar_pares_impares(anios):            # Cuenta cuántos años son pares y cuántos son impares.
    pares = 0
    impares = 0
    i = 0
    while i < len(anios):
        if anios[i] % 2 == 0:
            pares += 1
        else:
            impares += 1
        i += 1
    return pares, impares

def todos_despues_2000(anios):           # Devuelve True si todos los integrantes nacieron después del 2000.
    i = 0
    while i < len(anios):
        if anios[i] <= 2000:
            return False
        i += 1
    return True

def hay_bisiesto(anios):                #  Devuelve True si al menos un integrante nació en un año bisiesto.
    i = 0
    while i < len(anios):
        if es_bisiesto(anios[i]):
            return True
        i += 1
    return False

def producto_cartesiano(anios, edades):      # Muestra todas las combinaciones posibles de pares (año, edad) de los integrantes.
    print("\n--- Producto cartesiano años x edades ---")
    i = 0
    while i < len(anios):
        j = 0
        while j < len(edades):
            print("(", anios[i], ",", edades[j], ")")
            j += 1
        i += 1

anios = ingresar_anios()                   # Se ingresan los años de nacimiento y se cuentan cuántos son pares e impares.
pares, impares = contar_pares_impares(anios)
print("\nCantidad de años pares:", pares)
print("Cantidad de años impares:", impares)

if todos_despues_2000(anios):              # Si todos son mayores a 2000 → imprime "Grupo Z".
    print("Grupo Z")
if hay_bisiesto(anios):                    # Si alguno es bisiesto → imprime "Tenemos un año especial".
    print("Tenemos un año especial")            
edades = []
i = 0
while i < len(anios):        # Pide las edades actuales de los integrantes e Imprime el producto cartesiano de años × edades.
    edad = int(input("Ingrese la edad actual del integrante " + str(i+1) + ": "))
    edades.append(edad)
    i += 1
producto_cartesiano(anios, edades) 