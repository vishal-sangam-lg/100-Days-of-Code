student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    student = key
    marks = student_scores[key]
    if 91 <= marks <= 100:
        grade = "Outstanding"
    elif 81 <= marks <= 90:
        grade = "Exceeds Expectations"
    elif 71 <= marks <= 80:
        grade = "Acceptable"
    else:
        grade = "Fail"
    student_grades[student] = grade

# 🚨 Don't change the code below 👇
print(student_grades)
