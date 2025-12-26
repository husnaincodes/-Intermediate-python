def multiply_list(lst):
    
    product = 1
    for num in lst:
        product *= num
    return product

print(multiply_list([2, 3, 4]))
