
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

