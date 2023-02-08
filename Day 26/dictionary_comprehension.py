# Syntax:
# new_dict = {new_key:new_value for item in list if condition}
# new_dict = {new_key:new_value for (key, value) in old_dict.items() if condition}

import random
import pandas

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# Dictionary Comprehension with list
students_scores = {student: random.randint(1, 100) for student in names}
print(students_scores)

# Dictionary Comprehension with dictionary
passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)

# Exercise 1
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

words = sentence.split(" ")
word_len_dict = {word: len(word) for word in words}

print(word_len_dict)

# Exercise 2
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: (temp * 9 / 5) + 32 for (day, temp) in weather_c.items()}
print(weather_f)

#
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping in pandas dataframe
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# for (key, value) in student_data_frame.items():
#     print(value)

for (index, row) in student_data_frame.iterrows():
    print(index)
    print(row.student)
    print(row.score)
