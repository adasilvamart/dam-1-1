# A valid sudoku square satisfies these two properties:
#   1. Each column of the square contains each of the whole numbers from 1 to n exactly once.
#   2. Each row of the square contains each of the whole numbers from 1 to n exactly once.
# You may assume the the input is square and contains at least one row and column.


# Funcion para comprobar que no se repiten nºs en la fila  
def check_row(a):
    # Para cada fila en a
    for row in a:
        # Para cada item en la fila
        for item in row:
            # Si la cuenta del item es mayor de 1 devuelve False
            if row.count(item) > 1:
                return False
    # En caso de que no se repitan en la fila devuelve True
    return True

# Funcion para comprobar que no se repiten nºs en la columna
def check_col(a):
    # Indice para las columnas
    i = 0
    # Mientras el indice no sea igual al nº de filas en a
    while i < len(a):
        # La columna será el elemento de la fila según el índice de la lista
        col = [row[i] for row in a]
        # Para cada item de la columna
        for item in col:
            # Si la cuenta del item es mayor de 1 devuelve False
            if col.count(item) > 1:
                return False
        # Aumentamos el índice
        i += 1
    # En caso de que no se repitan en la columna devuelve False
    return True

# Funcion para comprobar el sudoku
def check_sudoku(a):
    # Para cada fila
    for row in a:
        # Para cada item en la fila
        for item in row:
            # Si el item no es un int o el valor supera el len(a)
            if type(item) != int or max(row) > len(a):
                # Devuelve False
                return False
    # Si no se repiten ni en las filas ni en las columnas devuelve True
    if check_row(a) and check_col(a):
        return True
    # Si no cumple ninguna de las condiciones devuelve False
    else:
        return False
    
    
correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [2,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
              [2,3,1,4],
              [4,1,2,3],
              [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
print(check_sudoku(correct))
print(check_sudoku(incorrect))
print(check_sudoku(incorrect2))
print(check_sudoku(incorrect3))
print(check_sudoku(incorrect4))
print(check_sudoku(incorrect5))