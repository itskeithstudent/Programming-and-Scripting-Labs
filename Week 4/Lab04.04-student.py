#Program to keep reading students until user enters a blank string
#will assume it's a name even if numbers are entered, so take user input as str

#take names from user
studentf_name = str(input("Enter a student first name please (BLANK to quit): ")) # we will only exit if first name is blank could have individuals like Cher with no last name
entered_students = [] #list of entered numbers
if studentf_name == '': #if user has entered a '' we proceed no further
    print("You entered no name")
else: #else user must not have entered a blank
    while studentf_name !='': #while user hasn't entered a blank
        #this list gets reassigned to empty at start of each loop
        student_name_list = []
        studentl_name = str(input("Enter a student last name please: "))
        student_name_list.append(studentf_name)
        student_name_list.append(studentl_name) 
        entered_students.append(student_name_list)#we don't need to add 0 to the end of the list when a user enter 0
        studentf_name = str(input("Enter a student name please (BLANK to quit): "))
    print("Here are the names of your students back again")
    #for loop over entered_students list, print first 2 index's of student
    for student in entered_students:
        print(f"{student[0]} {student[1]}")