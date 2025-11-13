
import random

# 8. Juego de adivinanza en Binario:
def binario_decimal():

    numero = random.randint(1,100)
    binario = bin(numero)[2:]
    print("Adivina el número: ", binario)
    respuesta = int(input("Ingresa el equivalente decimal: "))
    if respuesta == numero:
        print("Adivinaste")
    else:
        print("Fallaste, el número correcto es: ", numero)


#Se muestra el número decimal y luego el usuario tiene que adivinar en binario

def decimal_binario():
    decimal = random.randint(1,100)
    print("Adivina el número en binario: ", decimal)
    respuesta_binaria = input("Ingresa el equivalente en binario: ")
    if respuesta_binaria == bin(decimal)[2:]:
        print("Adivinaste")
    else:
        print("Fallaste, el número correcto es: ", bin(decimal)[2:])

#Menú para el juego de adivinanza

def juego_adivinanza():
    try:
        while True:
            opcion = int(input("Opcion 1: Adivinar decimal de binario\nOpcion 2: Adivinar binario de decimal\n Elige una opcion "))
            match opcion:
                case 1:
                    binario_decimal()
                case 2:
                    decimal_binario()
                case 3:
                    print("Saliendo del juego ")
                    break
    except ValueError:
        print("Valor no valido")
juego_adivinanza()

print("=== SIMULADOR DE PUERTAS LÓGICAS ===")
print("1 - AND")
print("2 - OR")
print("3 - NOT")
print("4 - NAND")
print("5 - NOR")
print("6 - XOR")

op = int(input("Seleccione una opción: "))

if op == 3:
    A = int(input("Ingrese el valor A (0 o 1): "))
else:
    A = int(input("Ingrese el valor A (0 o 1): "))
    B = int(input("Ingrese el valor B (0 o 1): "))

if A not in (0, 1) or (op != 3 and B not in (0, 1)):
    print("Error: solo se aceptan valores 0 o 1.")
    exit()

if op == 1:
    Z = A & B                        # AND
    nombre = "AND"

elif op == 2:
    Z = A | B                        # OR
    nombre = "OR"

elif op == 3:
    Z = 1 - A                        # NOT
    nombre = "NOT"

elif op == 4:
    Z = 1 - (A & B)                  # NAND
    nombre = "NAND"

elif op == 5:
    Z = 1 - (A | B)                  # NOR
    nombre = "NOR"

elif op == 6:
    Z = int(A != B)                  # XOR
    nombre = "XOR"

else:
    print("Opción inválida.")
    exit()

print("\n--- RESULTADO ---")
if op == 3:
    print(f"{nombre} {A}  →  {Z}")
else:
    print(f"{A}  {nombre}  {B}  →  {Z}")
