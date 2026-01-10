def find_item(data, target):

    for key, value in data.items():
        if isinstance(value, dict):

            result = find_item(value, target)
            if result:
                return [key] + result
        else:
            if target in value:
                return [key]
            
    return None
