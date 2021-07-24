def flatten_list(lol):
    if len(lol) == 0:
        return lol
    if isinstance(lol[0], list):
        return flatten_list(lol[0]) + flatten_list(lol[1:])
    return lol[:1] + flatten_list(lol[1:])


print(flatten_list(([[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5])))

