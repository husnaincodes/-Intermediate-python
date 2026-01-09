def combine_dicts(lst, index=0, result=None):
    if result is None:
        result = {}
    if index == len(lst):
        return result
    
    for k in lst[index]:
        result[k] = result.get(k, 0) + 1
    
    
    return combine_dicts(lst, index + 1, result)
