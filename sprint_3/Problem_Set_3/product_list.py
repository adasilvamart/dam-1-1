def product_list(col):
    res = 1
    for n in col:
        res *= n 
    return res

print(product_list([1, 2, 3, 4]))