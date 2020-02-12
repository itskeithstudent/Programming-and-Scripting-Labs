#

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

#print(student_dict["modules"]["coursename"])
for module in student_dict["modules"]:
    #surprisingly this won't work with double quotes but only single quotes
    #print(f"{module["coursename"]} {module["grade"]}")
    print(f"{module['coursename']} {module['grade']}")