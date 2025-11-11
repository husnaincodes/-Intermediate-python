students = {
    "Ali": "A",
    "Husnain": "B+",
    "Sara": "A-"
}

name = input("Enter student name to search: ")

if name in students:
    print(f"{name}'s grade is {students[name]}")
else:
    print("Student not found.")
