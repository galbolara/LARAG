tapay_name = input("Enter Name: ").title()

print(f"\nHello, I am {tapay_name}!")

tapay_choice = int(input("1. Power  2. Voltage  3. Current: "))

if tapay_choice == 1:
    voltage = float(input("V: "))
    current = float(input("I: "))
    tapay_result = voltage * current

elif tapay_choice == 2:
    power = float(input("P: "))
    current = float(input("I: "))
    tapay_result = power / current

elif tapay_choice == 3:
    power = float(input("P: "))
    voltage = float(input("V: "))
    tapay_result = power / voltage

else:
    print("Invalid choice.")
    exit()

print(f"{tapay_name}, Result = {tapay_result:.2f}")
