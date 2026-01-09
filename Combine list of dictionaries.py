def combine_dicts(lst, index=0, result=None):
    if result is None:
        result = {}

    
    print(f"Calling index = {index}, result = {result}")

    if index == len(lst):
        print("Reached end of list. Final result returned.")
        return result

    for k in lst[index]:
        result[k] = result.get(k, 0) + 1
        print(f"Updated key '{k}': {result}")

   
    print(f"Moving to next index: {index + 1}\n")

    return combine_dicts(lst, index + 1, result)
lst = [{'a': 1, 'b': 2}, {'a': 3}, {'c': 4}]
print(combine_dicts(lst))
