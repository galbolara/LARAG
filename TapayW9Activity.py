#input
Tapay_Name = input("Enter Name: ")
Tapay_TotalItems = int(input("Enter Total Items: "))
Tapay_Score = int(input("Enter score: "))

#Process
Tapay_Percent = Tapay_Score / Tapay_TotalItems * 100

#Output
if Tapay_Percent >=97 and Tapay_Percent <=100:
    color = "Dark Green"
elif Tapay_Score >=90 and Tapay_Score <=95:
    color = "light Green"
elif Tapay_TotalItems >=80 and Tapay_TotalItems <=89:
    color = "Yellow Green"
elif Tapay_Score >=70 and Tapay_Score <=79:
    color = "yellow"
elif Tapay_TotalItems >=60 and  Tapay_TotalItems <=69:
    color = "Orange"
elif (Tapay_Score >=0 and Tapay_Score<=60):
    color = "Red"
else:
    color = "Unknown due invalid Score"

    if Tapay_TotalItems >=60:
        result = "Passed"
result = "Failed"

print("\n ================== Student Score Result =====================")
print(f"Student Name: {Tapay_Name}")
print(f"Student Total Items: {Tapay_TotalItems}")
print(f"Student Score: {Tapay_Score}")
print(f"Student Percent: {Tapay_Percent:.2f}%")
print(f"color code based on students grade: {color}")
print(f"final students results on the system: {result}")

print ("\n ========== To be emailed to the students ============")
