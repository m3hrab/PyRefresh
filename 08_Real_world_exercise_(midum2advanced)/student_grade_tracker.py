"""
Exercise 1: **Student Grades Tracker**
You are given a list of student names and their respective grades in different subjects. Write a program to:
Calculate the average grade for each student.
Find students with the highest and lowest averages.

"""
students_grades = [
    ('Alice', [85, 90, 78]),
    ('Bob', [90, 92, 85]),
    ('Charlie', [88, 85, 91])
]


def grade_average(grades):
    """calculate the avarage grade"""
    
    average = sum(grades[1]) / len(grades[1])
    return average 

# Sort the student grade based on their average grade
# My newest solution after refreshing python
students_grades.sort(key=grade_average, reverse=True)

# My older Solution

# def avg(grade):
#     return sum(grade)/ len(grade)

# for i in range(len(students_grades)):
#     for j in range(i+1, len(students_grades)):
#         if avg(students_grades[i][1]) < avg(students_grades[j][1]):
#             temp = students_grades[i]
#             students_grades[i] = students_grades[j]
#             students_grades[j] = temp
            
# print(students_grades)


# Display the student rank
for student in students_grades:
    print(f"{student[0]} -> Average grade: {grade_average(student):.2f}")