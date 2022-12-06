colorlist = ['red','blue','yellow','green','purple','white']
print("you csn print one color. Index numbers go from 0 to", len(corlolist))
i = int(input("which color do you want to print"))
while i >= len(colorlist):
    i = int(input("Enter correct number:"))
    