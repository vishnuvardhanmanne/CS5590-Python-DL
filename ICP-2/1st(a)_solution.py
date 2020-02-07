lbs=[]
kgs=[]
n=int(input("enter number of elements:"))
for i in range(0,n):
    elements=int(input("Enter the weight of student in lbs>>"))
    lbs.append(elements)
    kgs.append(elements*0.45)
print(lbs)
print(kgs)