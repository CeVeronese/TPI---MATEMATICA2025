"""PARTE 1 FUNCIONES"""
try:
    import matplotlib.pyplot as plt

    def costo(x):
        a = 50
        b = 200
        return a * x + b
    def ganancia(x):
        p = 2
        q = 150
        r = -100
        return -p * x**2 + q*x + r

    x = int(input("Ingrese la cantidad de unidades producidas: "))
    c = costo(x)
    g = ganancia(x)
    print("Costo total: $", c)
    print("Ganancia neta: $", g)

    x_valores = []
    c_valores = []
    g_valores = []

    for i in range(0, 60):
        x_valores.append(i)
        c_valores.append(costo(i))
        g_valores.append(ganancia(i))
    plt.plot(x_valores, c_valores, label="Costo", color="blue")
    plt.plot(x_valores, g_valores, label="Ganancia", color="green")

    """--- punto de máxima ganancia ---"""
    p = 2
    q = 150
    x_max = q / (2 * p)
    g_max = ganancia(x_max)
    plt.scatter(x_max, g_max, color="red", label="Ganancia Máxima")
    plt.title("Costo y ganancia en función de la producción")
    plt.xlabel("Cantidad producida (x)")
    plt.ylabel("Dinero ($)")
    plt.legend()
    plt.grid(True)
    plt.show()

    """PARTE 3 - MATRICES"""
    #--- PRIMERA FUNCIÓN: Producto de dos matrices 2x2 ---
    def producto(A,B):
        resultado = [[0]*2 for i in range(2)]
        for i in range(2):
            for j in range(2):
                resultado[i][j] = A[i][0]*B[0][j] + A[i][1]*B[1][j]
        return resultado
    #   --- SEGUNDA FUNCIÓN: Transpuesta de una matriz 2x2 ---
    def transpuesta(M):
        T = [[0]*2 for i in range(2)]
        for i in range(2):
            for j in range(2):
                T[j][i] = M[i][j]
        return T
    #   --- TERCERA FUNCIÓN: Inversa de una matriz 2x2 ---
    def inversa_2x2(M):
        det = M[0][0]*M[1][1] - M[0][1]*M[1][0]
        if det == 0:
            return 0
        inv = [[0]*2 for i in range(2)]
        inv[0][0] = M[1][1]/det
        inv[0][1] = -M[0][1]/det    #cambia el signo del elemento b
        inv[1][0] = -M[1][0]/det    # cambia el signo del elemento c
        inv[1][1] = M[0][0]/det
        return inv
    #   --- CUARTA FUNCIÓN: Se muestra la matriz de forma ordenada ---
    def mostrar_matriz(nombre,M):
        print(nombre, "=")
        for i in range(2):
            print("[", end=" ")
            for j in range(2):
                print(round(M[i][j],2), end=" ")
            print("]")
        print()
    # -----------MATRICES-----------
    matrizA= [
        [10,20],
        [30,40]
    ]

    matrizB= [
        [5,2],
        [3,4]
    ]

    # -----------CÁLCULOS-----------
    valorTV = producto(matrizA, matrizB)
    matrizTA = transpuesta(matrizA)
    invB = inversa_2x2(matrizB)
    if invB != 0:
        identidad = producto(matrizB,invB)
    else:
        identidad = 0
    identidad = producto(matrizB, invB)

    # -----------RESULTADOS-----------
    mostrar_matriz("Matriz A", matrizA)
    mostrar_matriz("Matriz B", matrizB)
    mostrar_matriz("Valor total de ventas (A * B)", valorTV)
    mostrar_matriz("Transpuesta de A", matrizTA)
    if invB != 0:
        mostrar_matriz("Inversa de B", invB)
        mostrar_matriz("Verificación (B * B-1)", identidad)
    else:
        print("La matriz B no tiene inversa. Determinante = 0")

    """PARTE 5 - PRODUCTO CARTESIANO"""
    A = [18, 19, 20]
    B= [25, 26, 27]
    producto = [] # lista vacía para almacenar el producto cartesiano
    for i in range(len(A)):
        for j in range(len(B)):
            producto.append((A[i], B[j]))  # agregamos la tupla (estudiante, tutor) al producto cartesiano
    print("Combinaciones posibles de estudiante-tutor:")
    for i in range(len(producto)):
        print(producto[i])
        print()

    existe = False
    edadE = int(input("Ingrese la edad del estudiante: "))
    edadT = int(input("Ingrese la edad del tutor: "))

    for i in producto:
        if edadE == i[0] and edadT == i[1]:
            existe = True
    if existe == True:
        print("La combinación existe")
    else:
        print("La combinación no existe")
    print()
    print("Ejemplo Práctico: ")
    print("""
          Un programador está desarrollando un sistema que debe funcionar correctamente en 
          diferentes sistemas operativos y con distintos navegadores web.
          Conjunto A = {Windows, Linux, macOS}
          Conjunto B = {Chrome, Firefox, Edge}
          Se empareja cada sistema operativo con cada navegador
          """
          )

    print(f"El dominio es {edadE} y la imagen es {edadT}")
    print()
except Exception:
    print("Ingrese valores validos porfa")