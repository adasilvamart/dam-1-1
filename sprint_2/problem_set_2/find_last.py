def find_last(target, search):
    return target.rfind(search)
print(find_last("Holala", "la"))

last_pos = lambda target, search: target.rfind(search)
print(last_pos('holala', 'la'))