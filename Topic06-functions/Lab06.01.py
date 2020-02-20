###Initialising dict and list and choice
some_dict = {"StudentName":"Keith", "Subjects": ["Web App Development", "Programming and Scripting", "Computer Architecture"]}
list_of_dicts = [some_dict]
choice = ''

def prompt():
    #First I'm just using simple print, then store user input in user_in
    print("What would you like to do?\n (a) \n (v) \n (q)\n")
    user_in=input("Type a or v or q: ")
    print(f"You chose {user_in}")
    return user_in

def view(students):
    print(students)

def add():
    new_student = {}
    new_student["StudentName"]=str(input("Enter a student name: "))
    new_student["Subjects"]=subjects()
    return new_student

def quit():
    return 0

def subjects():
    return[]

while choice.lower() != 'q':
    choice = prompt()
    if choice.lower()=="a":
        list_of_dicts.append(add())
        add()
    if choice.lower()=="v":
        view(list_of_dicts)

view(list_of_dicts)

'''
user_choice = prompt()

#I don't care if user types in a or A, so casting str to all lowercase
if(user_choice.lower()=="a"):
        print("A")
elif(user_choice.lower()=="v"):
        print(f"{some_dict}")
elif(user_choice.lower()=="q"):
        print("Q")

'''