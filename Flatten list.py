def flatten(items):
    result = []
    for x in items:
        if isinstance(x, list):
            result += flatten(x)
        else:
            result.append(x)
    return result
print(flatten([1,23,45,64]))