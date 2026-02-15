d1 = {"Alice": 85, "Carol": 90}
name = input("Enter the student's name: ")
try:
    marks = d1[name]
    print(f"{name}'s marks: {marks}")
except KeyError:
    print("Student not found.")