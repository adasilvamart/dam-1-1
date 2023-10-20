
""" 
    La función devolverá los 'n' números 
    de la lista 'arr' conservando el orden.
'"""
def first_n_smallest(arr, n):
    # Hacemos una copia reversa de arr
    sol = arr[::-1]

    # Iterador de los elementos del arr
    i = len(arr)
    # Iteramos hasta 'n'
    while i > n:
        # Eliminando el máximo
        sol.remove(max(sol))
        i -= 1

    # Respuesta revertida para conservar el orden de 'arr'
    return sol[::-1]

numeros = [1, 2, 3, 2, -1]
print(first_n_smallest(numeros, 3))