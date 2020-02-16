#Lab 05 exercise 3 write a program that stores a student in a dict
# also stores a list of her courses within that dict

student_dict = {
    "name":"Mary",
    "modules": [
        {
            "coursename": "Maths",
            "grade": "A"
        },
        {
            "coursename": "Geography",
            "grade": "A++"
        }
        ]}

#loop through each item in student_dict key modules
for module in student_dict["modules"]:
    #surprisingly this won't work with double quotes but only single quotes
    #print(f"{module["coursename"]} {module["grade"]}")
    print(f"{module['coursename']} {module['grade']}")