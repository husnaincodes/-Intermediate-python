marks ={
    "HUSNAIN": 100,
    "SHAHBAZ": 98,
    "RAFAY"  : 88,
    "AHMAD" :  89,
    "list" : [1,4,5,6,7],
    "LAHORE" : 0,
    'AHMAD' : 89,
    # 0 : "LAHORE"
}
print(marks,type(marks))

print(marks["AHMAD"])
print(marks["HUSNAIN"])
print(marks["SHAHBAZ"])
print(marks["RAFAY"])
print(marks["list"])
# print(marks[0]) # it will give error because 0 is not a key in the dictionary     
print(marks.get("AHMAD"))
print(marks.get("HUSNAIN"))
print(marks.get("SHAHBAZ"))
print(marks.get("RAFAY"))
print(marks.get("list"))
print(marks.get(0)) # it will give None because 0 is not a key