balance = 200000
pin = "1234"
atm_pin = input("Enter the ATM pin : ")

if atm_pin==pin:
    
    amount = int(input("Enter the amount you want to withdraw : "))
    if amount <=balance:
        print("Your amount withdraw sucessfully!")
        print(f"Your balance in the bank after withdraw is : {balance-amount}")
    else:
        print("Invalid Balance")

else:
    print("Pin is invalid")

