import random

print("Hello there!")
firstname = input("What's Your name?")

# input names in the fields. 

first = ["Jim", "Joe", "john", "Bob", "Billy"]
last = ["Capone", "Dahlmer", "Mansion", "Jones", "Trump"]
namebank = []

while True:
    name = input("Do you want to generate a name? [y/n]:")
    if name.upper() == "Y":
        rand = random.randint(0, 4)
        randname = first[rand] + " " + last[rand]
        namebank.append(randname)
        print(f"Your new name is {randname}\n")
        continue
    else:
        print("Thank you for creating a new name")
    break
