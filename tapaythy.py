print("============= STUDENT NAMES AND PROGRAM ================")
print("________________________________________________________")
tapay_student=[("Jonah Perez", "BSCS", "1st year", 1),
          ("Alex Santos", "BSMT", "2nd year", 2),
          ("Micah Mendoza", "BSCS","2nd year", 2),
          ("Allen Torres", "BSMT", "1st year", 1),
          ("Dean Marcos", "BSCS", "4th year", 4),
          ("Won Zi", "BSCS", "3rd year", 3),
          ("Philip Ligan", "BSMT" , "4th year", 4),
          ("Lara Tapay" , "BSCS", "3rd Year", 3)]

tapay_course = input("Choose Course (BSCS/BSMT):").upper()
print("_____________________________________________________")
print("================= Student Information ===============")
print("_____________________________________________________")

for tapay_student in tapay_student:
  if tapay_student[1] == tapay_course:
    print("Name:", tapay_student[0])
    print("Program: ", tapay_student[1])
    print("Year:", tapay_student[2])
    print()


