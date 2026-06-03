# List
student_marks = [85, 45, 72, 95, 45]

print("Student Marks:", student_marks)

# Set
unique_marks = set(student_marks)
print("Unique Marks:", unique_marks)

# For Loop + If Else
print("\nResults:")

for mark in student_marks:

    if mark >= 50:
        print(mark, "- Pass")

    else:
        print(mark, "- Fail")

# Nested If
age = 20
has_id = True

if age >= 18:
    if has_id:
        
        print("\nEntry Allowed")
    else:
        print("\nID Required")

# While Loop
print("\nCountdown:")

count = 5

while count > 0:
    print(count)
    count -= 1

# Multiplication Table
print("\nTable of 5")

for i in range(1, 11):
    print("5 x", i, "=", 5 * i)