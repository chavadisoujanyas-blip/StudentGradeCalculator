name = input("Enter Student Name: ")

maths = int(input("Maths: "))
science = int(input("Science: "))
english = int(input("English: "))

total = maths + science + english
percentage = total / 3

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
else:
    grade = "C"

print("\nStudent:", name)
print("Total:", total)
print("Percentage:", round(percentage, 2))
print("Grade:", grade)