###Initialising dict and list and choice
#some_dict = {"StudentName":"Keith", "Subjects": ["Web App Development", "Programming and Scripting", "Computer Architecture"]}
import json
list_of_dicts = []
choice = ''

#function to prompt user for what they would like to do
def prompt():
    #First I'm just using simple print, then store user input in user_in
    print("What would you like to do?\n (a) \n (v) \n (q)\n")
    user_in=input("Type a or v or q: ")
    print(f"You chose {user_in}")
    return user_in

def showSubjects(subjects):
    print("\tName   \tGrade")
    for subject in subjects:
        print(f"\t{subject['name']}   \t{subject['grade']}")

#simple function that just shows dictionary of students
def view(students):
    for student in students:
        print("student name")
        print(student['StudentName'])
        showSubjects(student['Subjects'])

#function to add a new student
def add():
    new_student = {}
    new_student["StudentName"]=str(input("Enter a student name: "))
    new_student["Subjects"]=subjects()
    return new_student

#function to exit loop
def quit():
    return 0

#function to add subjects per user
def subjects():
    subject_list = []
    new_subject = str(input("Enter your subjects (blank to stop)"))
    while(new_subject != ''):
        subject = {}
        subject["name"] = new_subject
        subject["grade"] = int(input('Enter a grade:'))
        subject_list.append(subject)
        new_subject = str(input("Enter your subjects (blank to stop)"))
    print(subject_list)
    return subject_list

def saveToFile():
    with open("test.txt", "wt") as file:
        json.dump(list_of_dicts,file)

def loadFromFile():
    global list_of_dicts
    with open("test.txt", "rt") as file:
        list_of_dicts=json.load(file)
        print(list_of_dicts)

choice = prompt()
while choice.lower() != 'q':
    #print(list_of_dicts)
    if choice.lower()=="a":
        list_of_dicts.append(add())
    if choice.lower()=="v":
        view(list_of_dicts)
    if choice.lower()=='s':
        saveToFile()
    if choice.lower()=='l':
        loadFromFile()

    choice = prompt()

view(list_of_dicts)

print(list_of_dicts)