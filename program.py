
number = int(input("Enter your number :"))


for i in range (1,number+1):
    print(" "*(number-i),end="")
    print("*"*(2*i-1),end="")
    print("")