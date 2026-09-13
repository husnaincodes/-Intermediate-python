name  = input("Enter your name: ")

for ch in name :
    if ch.isalpha():
        print(ch, "is an alphabet.")
    elif ch.isdigit():
        print(ch, "is a digit.")
    else:
        print(ch, "is a special character.")



name2 = input("Enter your name: ")
count = 0
for ch in name2 :
    if ch.lower() in 'aeiou':
        count = count + 1
        print(ch, "is a vowel.")
        