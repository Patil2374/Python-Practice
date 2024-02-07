from sys import *
Student_marks = [98,56,65,78,83,88,91,50,40]
Score = [Student_marks if Student_marks>=60 else 'NONE' for Student_marks in range(len(Student_marks)) ]
print(Score)
print()
for i in range(len(Student_marks)):
    print(Score[i])
print()


