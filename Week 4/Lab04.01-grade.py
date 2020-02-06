#program to  read students mark and print whether pass or fail

student_grade = int(input("Tell me what percentage you got and I'll tell you the grade..."))

#check first that we got a possible grade between 0 and 100
if student_grade < 0 or student_grade > 100:
    print("Enter a possible number dumbo!")
elif student_grade < 40: #less than 40
    print("FAIL")
elif student_grade < 49: #less than 49
    print("PASS")
elif student_grade < 59: #less than 59
    print("Merit 2")
elif student_grade < 69: #less than 69
    print("Merit 1")
else: #70 or greater
    print("Distinction")