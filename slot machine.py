Max_lines = 3
MAX_BET = 100
MIN_BET = 1
def deposit():
    while True:
        amount = input("What would you like deposit? $: ")
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Enter only digit")
    return amount

def get_the_lines():

    while True:
        lines = input(f"Enter the number of lines you bet on (1-{str(Max_lines)}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1<=lines<=Max_lines:
                break
            else:
                print("Enter a valid  number of lines")
        else:
            print("Enter only digit")
    return lines

def get_bet():
    while True:
        amount = input("what would you bet? :$")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET<=amount<=MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET}-${MAX_BET}")
        else:
            print("Enter only digit")
    return amount





def main():
    balance = deposit
    lines = get_the_lines
    print(balance,lines)
