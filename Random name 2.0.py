import random

print("Hello there!")
firstname = input("What's Your name?")

# New Class Name Generator. Insert more name if needed.  

first = ["CARPE SCHEME", "TEAM BONSI", "DNS"]
namebank = []

while True:
    name = input("Do you want to generate a new name? [y/n]:")
    if name.upper() == "Y":
        rand = random.randint(0, 3)
        randname = first[rand]
        namebank.append(randname)
        print(f"Your new name is {randname}\n")
        continue
    else:
        print("Thank you for creating a new name")
    break

