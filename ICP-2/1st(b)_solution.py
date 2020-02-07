n = int(input("Please enter the number of students: "))
lbs = []
kgs = []
for i in range(n):
        k = float(input("Enter the weight of student in lbs>>"))
        lbs.append(k)
kgs = [lbs[x] * 0.453592 for x in range(n)]
print(kgs)
