#program to  read students mark and print whether pass or fail

student_grade = int(input("Tell me what percentage you got and I'll tell you the grade..."))
if student_grade < 40:
    print("FAIL")
elif student_grade < 49:
    print("PASS")
elif student_grade < 59:
    print("Merit 2")
elif student_grade < 69:
    print("Merit 1")
else:
    print("Distinction")