# Define una rutina que devuelve True si una matriz es
# antisimetrica y False en otro caso. 
# Una matriz n * n es antisimetrica si se verifica que 
# sus elementos mantienen la relación:
# matriz[i][j] = - matriz[j][i] 
# para cada i=0,1,...,n-1 y para cada j=0,1,...,n-1.

def esAntisimetrica(matriz):
    
    # i recorre las filas, j los elementos
    for i in range(len(matriz)):
        for j in range(len(matriz)):

            # Si cumple la condición para NO ser antisimétricas False
            if matriz[i][j] != - matriz[j][i]:
                return False
            
    # Devuelve True
    return True

if __name__ == '__main__':

    print(esAntisimetrica([[0, 1, 2], 
                           [-1, 0, 3], 
                           [-2, -3, 0]]))
    #>>> True

    print(esAntisimetrica([[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]]))
    #>>> True

    print(esAntisimetrica([[0, 1, 2], 
                        [-1, 0, -2], 
                        [2, 2,  3]]))
    #>>> False

    print(esAntisimetrica([[1, 2, 5],
                        [0, 1, -9],
                        [0, 0, 1]]))
    #>>> False

    # casos test que no satisfacen la precondicion de que la matriz sea cuadrada (assert)

    matriz4 = [[1,0,0,0],
               [0,1,1,0],
               [0,0,0,1]]

    print(esAntisimetrica(matriz4))
    #>>>False

    matriz5 = [[1,0,0,0,0,0,0,0,0]]

    print(esAntisimetrica(matriz5))
    #>>>False