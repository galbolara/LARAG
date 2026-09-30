patients={"Rhea": ("100,200,300"),
          "Alex": ("100,200,300")}

normal=120
for key,value in patients.items():
    print(key)
    for v in value:
        if v>normal:
            print(v,"normal")