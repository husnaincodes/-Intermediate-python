def remove_duplicates(lst):

    if len(lst) <= 1:
        return lst
    rest = remove_duplicates(lst[1:])
    if lst[0] == rest[0]:
        
        return rest
    return [lst[0]] + rest
