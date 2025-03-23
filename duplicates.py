# First, create a dictionary that consists of - id, name, class and subject integration of students. Then, write a program to retrieve unique entries and eliminate the rest.

student_data  =  {
    "id1":{"Name":"Hardik",
           "class":8,
           "Subject":["Physics","Maths","Games"]
           },
    "id2":{"Name":"Hardik",
           "class":4,
           "Subject":["Maths","Games"]
           },
    "id3":{"Name":"Hardik",
           "class":8,
           "Subject":["Physics","Maths","Games"]
           },
}
result = {}
for key,value in student_data.items():
    if value not in result.values():
        result[key]=value
print(result)
