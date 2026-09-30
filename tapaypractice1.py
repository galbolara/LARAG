#Practice 1

students = {
    "Ana": 85,
    "Ben": 90,
    "Carlo": 78,
    "Diana": 95,
}
print("STUDENTS GRADES")
print("-----------------------")
print("Ana:", students["Ana"])
print("Ben:", students["Ben"])
#Add a new student
students["Ella"] =88
#update a student's grade
students["Carlo"] = 82
students["Diana"] = 91
name1 = input("Enter students name: ")
grade1 = int(input("Enter grade: "))
students[name1] = grade1
print(students)
print("\nUpdated Student Grades")
print("-------------------------------")
for name, grade in students.items():
    print(name, ":", grade)
    #Search for a student
    search = input("\nEnter student name to search: ")
    if search in students:
        print(search, "has a grade of", students[search])
    else:
        print("student not found.")
        highest = max(students, key=students.get)
        print(highest)
