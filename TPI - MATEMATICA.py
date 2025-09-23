def ingresar_dnis():
    dnis = []
    n = int(input("¿Cuántos DNIs quiere ingresar?: "))
    i = 0
    while i < n:
        dni = input("Ingrese DNI " + str(i+1) + ": ")
        dnis.append(dni)
        i += 1
    return dnis

def digitos_unicos(dni):
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

def union(d1, d2):
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

def interseccion(d1, d2):
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

def diferencia(d1, d2):
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

def diferencia_simetrica(d1, d2):
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

def contar_frecuencias(dni):
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

def suma_digitos(dni):
    suma = 0
    i = 0
    while i < len(dni):
        suma += int(dni[i])
        i += 1
    return suma

dnis = ingresar_dnis()
lista_unicos = []
i = 0
while i < len(dnis):
    unicos = digitos_unicos(dnis[i])
    lista_unicos.append(unicos)

    if len(unicos) > 6:
        print("DNI", i+1, "-> Diversidad numérica alta")

    i += 1

print("\n--- Operaciones entre pares ---")
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

print("\n--- Frecuencias y Sumas ---")
i = 0
while i < len(dnis):
    contar_frecuencias(dnis[i])
    print("Suma de dígitos:", suma_digitos(dnis[i]))
    i += 1

print("\n--- Condiciones Globales ---")
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

#AÑOS
def ingresar_anios():
    anios = []
    n = int(input("¿Cuántos integrantes?: "))
    i = 0
    while i < n:
        anio = int(input("Ingrese año de nacimiento del integrante " + str(i+1) + ": "))
        anios.append(anio)
        i += 1
    return anios

def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

def contar_pares_impares(anios):
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

def todos_despues_2000(anios):
    i = 0
    while i < len(anios):
        if anios[i] <= 2000:
            return False
        i += 1
    return True

def hay_bisiesto(anios):
    i = 0
    while i < len(anios):
        if es_bisiesto(anios[i]):
            return True
        i += 1
    return False

def producto_cartesiano(anios, edades):
    print("\n--- Producto cartesiano años x edades ---")
    i = 0
    while i < len(anios):
        j = 0
        while j < len(edades):
            print("(", anios[i], ",", edades[j], ")")
            j += 1
        i += 1

anios = ingresar_anios()
pares, impares = contar_pares_impares(anios)
print("\nCantidad de años pares:", pares)
print("Cantidad de años impares:", impares)

if todos_despues_2000(anios):
    print("Grupo Z")
if hay_bisiesto(anios):
    print("Tenemos un año especial")
edades = []
i = 0
while i < len(anios):
    edad = int(input("Ingrese la edad actual del integrante " + str(i+1) + ": "))
    edades.append(edad)
    i += 1
producto_cartesiano(anios, edades) 