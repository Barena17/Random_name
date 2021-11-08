import random

# input names in the fields. 

first = ["Jim", "Joe", "john", "Bob", "Billy"]
last = ["Capone", "Dahlmer", "Mansion", "Jones", "Trump"]
namebank = []

while True:
    name = input("Do you want to generate a name? [y/n]: ")
    if name.upper() == "Y":
        rand = random.randint(0, 3)
        randname = first[rand] + " " + last[rand]
        namebank.append(randname)
        print(f"Your new name is {randname}\n")
        continue
    if name.upper == "N":
        print("Thank you for creating a new name")
    break