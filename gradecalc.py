print(" -----Student Grade Calculator ----")
name = input("Enter student name: ")
math = float(input("Enter Maths marks: "))
science = float(input("Enter Science marks: "))
english = float(input("Enter English marks: "))
social = float(input("Enter Social marks: "))
computer = float(input("Enter Computer marks: "))

total = math + science + english + social + computer
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n===== Result =====")
print("Student Name:", name)
print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")
print("Grade:", grade)

if grade == "F":
    print("Result: Fail")
else:
    print("Result: Pass")