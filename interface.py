#porgram inerface should have all of these:
#1. Tell the user what the porgram is and what is can do
#2. Tell the user make chices or select option
#3. Let the user enter information -you shoulc include a helpful message
#4. display result or answer
#5. Let the user close the porgram

teamlist = []

whille choice != 'X'
    print("TEAM MANAGER")
    print("============")
    print("This program will help you manage your team")
    print("\n")
    print("A: Append a value") 
    print("B: Prine the team list")
    print("X: Exit the progam")
    choice = input("Enter your choice: ")
if choice == "A":
    name = input ("Enter a name: ")
    teamlist.append(name)
print(teamlist)