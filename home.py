name = input("name: ")
surename = input("surname: ")
age = int(input("age: "))
if age >= 120:
    print(f'Mr {name} {surename}, you are joking.you are dead)).')
elif age >= 80:
    print(f"hello {name} {surename} you are very old for this ")
elif age >= 18:
    print(f"hello {name} {surename}.welocome.\n")
else:
    age2 = str(18 - age)
    print(f"hello {name} {surename}. you can come back after {age2} years.")
