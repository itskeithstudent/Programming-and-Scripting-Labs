#program to  read students mark and print whether pass or fail

#formerly student_grade was assumed to be an int
student_grade = float(input("Tell me what percentage you got and I'll tell you the grade..."))

#we must also check for the event that the student_grade is 0.5 or less off the next grade
#in which case they get rounded up to the next grade
#2 ways to do this, first is that we would round up every user input  
#other simpler way is just to edit the if statements and decrease value of each by 0.5 except for last one
#check first that we got a possible grade between 0 and 100
if student_grade < 0 or student_grade > 100:
    print("Enter a possible number dumbo!")
elif student_grade < 39.5: #less than 40
    print("FAIL")
elif student_grade < 48.5: #less than 49
    print("PASS")
elif student_grade < 58.5: #less than 59
    print("Merit 2")
elif student_grade < 69.5: #less than 69
    print("Merit 1")
else: #70 or greater
    print("Distinction")