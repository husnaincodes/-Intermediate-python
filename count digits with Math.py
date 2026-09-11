from math import log10 

def count_digits(num):
    if num == 0:
        return 1
    return int(log10(num)) + 1 

num = int(input("Enter a number: "))


print("Number of digits in", num, "is:", count_digits(num))