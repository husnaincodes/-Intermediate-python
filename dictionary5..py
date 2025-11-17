s = input("Enter the word: ")
my_dictionary = []
for i in range (len(s)):
    char = s[i]
    if char not in my_dictionary:
        count = 0
        for j in range(len(s)):
            if s [j]==char:
                count+=1
        print(f"{char}:{count}")