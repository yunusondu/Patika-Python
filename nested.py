def reverse_list(l):
    result = []
    for e in l:
        if isinstance(e, list):
            result.append(reverse_list(e))
        else:
            result.append(e)
    result.reverse()
    return result


print(reverse_list([[1, 2], [3, 4], [5, 6, 7]]))
