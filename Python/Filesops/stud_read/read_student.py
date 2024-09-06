f = open("D:\luminarjune\Filesops\student.txt","r")

students = []

for stud in f :

    students.append(stud.rstrip("\n"))


print(students)