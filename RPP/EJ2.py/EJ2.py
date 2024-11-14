matriz = [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

for j in range(len(matriz[0])):
    for i in range(len(matriz)):
        print(matriz[i][j], end= " ")

    print("")

    def medida_geometr_filas_colum(matriz):
        
        n = len(matriz)
        for fila in matriz:
            if len(fila) != n:
                print("La matriz debe ser cuadrada")

        medias_filas = []
        for fila in matriz:
            producto = 1
            for valor in fila:
                producto *= valor
            medias_fila = producto ** (1 / n)

        medias_filas.append(medias_fila)

        medias_columnas = []
        for i in range(n):
            producto = 1
            for j in range(n):
                producto *= matriz[j][i]
            media_columna = producto ** (1 / n)

            medias_columnas.append(media_columna)
        
            return medias_filas, medias_columnas
        
    medias_filas, medias_columnas = medida_geometr_filas_colum(matriz)
    print(f"La medida geometrica de filas es: {medias_filas}")
    print(f"La medida geometrica de columnas es: {medias_columnas}")

    def suma_diagonales(matriz):
        
        n = len(matriz)
        suma_principal = 0
        for i in range(n):
            suma_principal += matriz[i][i]

        suma_secundaria = 0
        for i in range(n):
            suma_secundaria += matriz[i] [n - 1 - i]
            

            return suma_principal, suma_secundaria
        
    suma_principal, suma_secundaria = suma_diagonales(matriz)
    print(f"La suma de la diagonal principal es: {suma_principal}")
    print(f"La suma de la diagonal secundaria es: {suma_secundaria}")

    matriz_EJ3 = [
        [1, 2, 8],
        [4, 3, 7],
        [6, 2, 3]
    ]
    
    def trans(matriz):
        n = len(matriz)
        transpuestaTemp = []
        
        for i in range (n):
            fila_transpuesta = []

            for j in range(len(matriz[i])):
                fila_transpuesta.append(matriz[j][i])

            transpuestaTemp.append(fila_transpuesta)

        return transpuestaTemp
        
print(trans(matriz_EJ3))

def suma_diagonales (matriz, diagonal = "ambas"):
    n = len(matriz)
    for fila in matriz:
        if len(fila) != n:
            print("La matriz debe ser cuadrada")

    suma_principal = 0
    suma_secundaria = 0

    for i in range (n):
        suma_principal += matriz[i][i]
        suma_secundaria += matriz[i][n - 1 - i]

    if diagonal == "principal": 
        return suma_principal
    elif diagonal == "secundaria":
        return suma_secundaria
    elif diagonal == "ambas":
        return suma_principal + suma_secundaria
    else:
        print("El parametro diagonal tiene que ser principal, secundaria o de ambas")

    suma_de_ambas = suma_diagonales(matriz, diagonal = "ambas")
    suma_de_principal = suma_diagonales(matriz, diagonal = "principal")
    suma_de_secundaria = suma_diagonales(matriz, diagonal = "secundaria")

    print(f"La suma de ambas diagonales es: {suma_de_ambas}")
    print(f"La suma de la diagonal principal es: {suma_de_principal}")
    print(f"La suma de la diagonal secundaria es: {suma_de_secundaria}")