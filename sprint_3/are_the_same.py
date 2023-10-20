"""
    La funcion debe devolver True si 'b'
    contiene los cuadrados la lista 'a'
"""
def comp(a, b):
    
    # Si alguno es None devuelve falso
    if a is None or b is None:
        return False
    else:
        # Guarda en res el cuadrado de los nums en 'a'
        res = [n * n for n in a]

        # Compara si es igual al array 'b'
        return sorted(b) == sorted(res)

list_1 = [-121, 144, 19, 161, 19, 144, 19, 11] 
list_1_sq = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

list_2 = [121, 144, 19, 161, 19, 144, 19, 11]  
list_2_sq = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]

print(comp(list_1, list_1_sq))
print(comp(list_2, list_2_sq))