number = int(input("Enter your number : "))


for i in range(2,number):
    if(number%i)==0:
        print("It is not a Prime number ")
        break
else:
    print("Your number is a prime number ")