goals=[]
#append value
for i in range(5):
    new = input("Add a new goal to the list: ")
    goals.append(new)
print(goals)
#edit an item
i = int (input("which goal do you ewant pt change: "))
goals[i-1] = input("eneter a new goal: ")
print(goals)

#delet an item
i =  int(input("which goal do you want to delete? "))
del goals [i-1]
print(goals)