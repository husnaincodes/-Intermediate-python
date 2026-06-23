nums = int(input("Enter a number: "))

while nums > 0:
    digit = nums % 10
    print(digit)
    nums = nums // 10   