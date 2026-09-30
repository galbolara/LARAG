from tapaypractice1 import highest

students = {
    "ana": [90,85,82],
    "kirk": [72,73,78],
    "liza": [69,71,83],
}
highest = 0
namehighest = ""
tally = 0
name75 = []
for name, grade in students.items():
    average = sum(grade) / len(grade)
    print(name, *grade, "Average:", round(average, 2))
if average > highest:
    highest = average
    namehighest = name
for g in grade:
    if g < 75:
        tally = tally + 1
        if name not in name75:
            name75.append(name)
print()
print("Highest average is", round(highest, 2))
print(f"fCongratulations, {namehighest}!")
print(f"There are {tally} grades below 75. Owned by { ', '.join(name75)}")