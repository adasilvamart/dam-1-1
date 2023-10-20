def median(x, y, z):
    big = max(x, y, z)
    if big == x:
        return max(y, z)
    elif big == y:
        return max(x, z)
    else:
        return max(x, y)

print(median(1, 3, 4))
print(median(8, 6, 2))
print(median(2, 4, 12))