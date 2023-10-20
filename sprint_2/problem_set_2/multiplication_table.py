def table(n):
    i = 1
    while i <= n:
        j = 1
        while j <= n:
            print(str(i) + " * " + str(j) + " = " + str(i * j))
            j += 1
        i += 1
    pass

print(table(10))