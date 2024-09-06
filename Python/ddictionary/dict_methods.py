student = {"name" : "sabari","course" : "fullsatck","place" : "kerala"}

# update the course as datascience in iteration

# for i in student :

#     if i == "course" :

#         student[i] = "datascience"

# print(student)

# delete a key "place" if it si present in dict using iteration

for i in student :

    if i == "place" :

        student.pop(i)

print(student)