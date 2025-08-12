
marks ={
    "HUSNAIN": 100,
    "SHAHBAZ": 98,
    "RAFAY"  : 88,
    "AHMAD" :  89,
    "list" : [1,4,5,6,7]
   
}
print(marks,type(marks))

print(marks.items())
print(marks.keys())
marks.update({"HUSNAIN": 87, "MAZZ":97})
print(marks)
print(marks.get("HUSNAIN"))
print(marks["HUSNAIN"])


# print(marks.get("HUSNAIN2")) #none


# The difference between these two is one give you an error if name is not in the marks (marks["HUSNIAn")
# and other gives you NONE                                                                                        
# print(marks["HUSNAIN2"]) #error

my_dict = { 55 : "husnain", "shahbaz" : 100}

n =len(my_dict)
print(n)
