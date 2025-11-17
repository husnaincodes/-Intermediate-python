names = ["Ali","Sara","Ahmad","Husnain","Sana","Hammad"]
result = {}
for  name  in names:
    first_letter = name[0]
    if first_letter in result:
        result[first_letter]+=1
    else:
        result[first_letter]=1
print(result)
