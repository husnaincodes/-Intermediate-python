nums = [1 ,3 ,4,5,6,7]
print(type(nums))
unique = set(nums)
print(type(unique))
if 8 in nums:
    print("True")
elif len(unique)==6:
    print("All unique")
else:
    print("Forward")