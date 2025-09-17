import math
num1 = int(input("Enter the first side number: "))
num2 = int(input("Enter the second side number: "))
num3 = int(input("Enter the thrid side number: "))
sum_sides =(num1+num2+num3)/2
area = float(math.sqrt(sum_sides*(sum_sides-num1)*(sum_sides-num2)*(sum_sides-num3)))
triangle_area = float(area)
print(f" The area of Triangle is : {triangle_area}")  