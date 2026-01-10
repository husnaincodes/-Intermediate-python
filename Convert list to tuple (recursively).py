def list_to_tuple(lst):

    if not lst:
        return ()
    return (lst[0],) + list_to_tuple(lst[1:])
print(list_to_tuple([1,23,45,667,5,10]))