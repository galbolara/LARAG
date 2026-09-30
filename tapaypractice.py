patients={"Rhea":(105,130,400),
          "Alex":(80,90,100)}
print(patients)
normal=120
for key, value in patients.items():
    #print(key,value)
    print(value)
for v in value:
    if value<normal:
     if value>normal:
        print(key,"diabetic")


